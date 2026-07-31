import pytest
from fastapi.testclient import TestClient
from src.main import app, expenses_db

# Initialize the test client
client = TestClient(app)

# This is a "fixture". It runs automatically before every single test 
# to empty the database. This ensures one test doesn't interfere with another.
@pytest.fixture(autouse=True)
def reset_db():
    expenses_db.clear()

def test_create_expense():
    response = client.post("/expenses", json={
        "title": "Coffee",
        "amount": 5.50,
        "category": "Food",
        "date": "2026-08-01"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Coffee"
    assert "id" in data  # Proves the UUID was generated

def test_get_expenses():
    # Insert dummy data first
    client.post("/expenses", json={
        "title": "Bus Ticket",
        "amount": 2.50,
        "category": "Travel",
        "date": "2026-08-01"
    })
    
    response = client.get("/expenses")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["category"] == "Travel"

def test_calculate_totals():
    # Insert two expenses
    client.post("/expenses", json={"title": "Apples", "amount": 10.00, "category": "Food", "date": "2026-08-01"})
    client.post("/expenses", json={"title": "Bananas", "amount": 15.00, "category": "Food", "date": "2026-08-01"})
    
    response = client.get("/expenses/total")
    assert response.status_code == 200
    assert response.json()["total_amount"] == 25.00

def test_delete_expense():
    # 1. Create an expense and grab its ID
    create_response = client.post("/expenses", json={
        "title": "Movie", "amount": 15.00, "category": "Entertainment", "date": "2026-08-01"
    })
    expense_id = create_response.json()["id"]

    # 2. Delete it
    delete_response = client.delete(f"/expenses/{expense_id}")
    assert delete_response.status_code == 200

    # 3. Verify it's gone
    get_response = client.get("/expenses")
    assert len(get_response.json()) == 0

def test_delete_nonexistent_expense():
    response = client.delete("/expenses/fake-id-123")
    assert response.status_code == 404