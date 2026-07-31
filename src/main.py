from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from datetime import date
from typing import List, Optional
import uuid

# --- DATA MODELS ---

# What the user sends to create an expense
class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category: str
    date: date

# The full expense object (inherits everything from ExpenseCreate and adds an ID)
class Expense(ExpenseCreate):
    id: str

# --- APP INITIALIZATION ---

app = FastAPI(
    title="Smart Expense Tracker API",
    description="A simple REST API to manage personal expenses.",
    version="1.0.0"
)

# Temporary in-memory storage (you will replace this with JSON file logic later)
expenses_db: List[Expense] = []

# --- ENDPOINTS ---

@app.get("/")
def read_root():
    return {"status": "success", "message": "Welcome to the Smart Expense Tracker API"}
@app.post("/expenses", response_model=Expense, status_code=201)
def create_expense(expense_in: ExpenseCreate):
    # 1. Create the new expense object with a generated UUID
    new_expense = Expense(
        id=str(uuid.uuid4()),
        **expense_in.model_dump()  # This cleanly unpacks title, amount, category, and date
    )
    
    # 2. Add it to our temporary list (you'll change this to JSON file saving later)
    expenses_db.append(new_expense)
    
    # 3. Return the created object so the user sees the new ID
    return new_expense
@app.get("/expenses", response_model=List[Expense])
def get_expenses(category: Optional[str] = Query(default=None, description="Filter expenses by category")):
    # If the user provided a category, filter the list
    if category:
        # We use .lower() to make the search case-insensitive (e.g., 'food' matches 'Food')
        filtered_expenses = [
            expense for expense in expenses_db 
            if expense.category.lower() == category.lower()
        ]
        return filtered_expenses
    
    # If no category was provided, return everything
    return expenses_db
@app.get("/expenses/total")
def get_total_expenses(category: Optional[str] = Query(default=None, description="Calculate total for a specific category")):
    # 1. If a category is provided, sum only those expenses
    if category:
        total = sum(expense.amount for expense in expenses_db if expense.category.lower() == category.lower())
        return {"category": category, "total_amount": total}
    
    # 2. If no category, sum all expenses
    total = sum(expense.amount for expense in expenses_db)
    return {"category": "all", "total_amount": total}
@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: str):
    # Enumerate gives us both the index number and the expense object as we loop
    for index, expense in enumerate(expenses_db):
        if expense.id == expense_id:
            # Remove the item from the list using its index
            expenses_db.pop(index)
            return {"status": "success", "message": f"Expense {expense_id} deleted."}
    
    # If the loop finishes and we didn't find the ID, return a 404 error
    raise HTTPException(status_code=404, detail="Expense not found")