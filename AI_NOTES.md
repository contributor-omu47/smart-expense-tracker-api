<!-- Data Validation & Models

AI Generated: I used the AI to generate the Pydantic models (ExpenseCreate and Expense) to handle data validation.

Validation/Changes: I reviewed the models to ensure they map exactly to the assignment requirements (id, title, amount, category, date). I decided to use Python's built-in date type for strict date validation rather than a simple string, and split the models into create/read representations to handle ID generation securely on the backend. -->

AI Generated: Used the AI to generate the GET /expenses/total logic.

Validation/Changes: I verified that it fulfills both the overall and category-specific total requirements. I accepted the AI's use of Python's sum() with a generator expression as it provides a clean, Pythonic way to calculate the totals without writing verbose loops. I also confirmed we are sticking to in-memory storage as permitted by the instructions to keep the architecture clean and focused.

overall questions asked in assignments:

# AI Usage Notes

For this assignment, I used AI as a pair programmer to help with boilerplate code and framework-specific syntax, while I focused on the core logic and making sure the API met all the requirements.

### 1. Which parts of the code were AI-generated vs. written by you
AI-Generated: I used the AI to generate the initial FastAPI project structure, the `requirements.txt` file, and the basic syntax for the Pydantic data models (`Expense` and `ExpenseCreate`). I also used it to quickly generate the skeleton for the `pytest` file.
Written/Driven by Me: I wrote and modified the actual business logic inside the endpoints. For example, I wrote the logic to calculate the totals using Python's `sum()`, implemented the `DELETE` logic with proper error handling, and figured out how to fix Windows-specific virtual environment bugs while testing locally. 

### 2. What you validated, tested, or changed in the AI's output, and why
Fixing the Swagger UI: The AI initially wrote the category filter as `category: Optional[str] = None`. I tested this locally and realized the input box wasn't showing up in the `/docs` page. I researched and changed this to use FastAPI's `Query(default=None)` object, which fixed the bug and allowed me to add a custom description for the UI.
Case-Insensitive Searching: I realized that if a user typed "food" but the database had "Food", the filter would fail. I manually updated the AI's search logic to use `.lower()` on both strings so the API is more user-friendly.
Error Handling: I tested the `DELETE` endpoint and realized deleting a fake ID didn't give a clear error. I updated the code to specifically raise a `404 HTTPException` so the API behaves like a standard REST application.
Test Isolation: Because I am using an in-memory list, I realized the tests would interfere with each other. I specifically set up a `@pytest.fixture` to clear the list before every single test to guarantee they were isolated.

### 3. Any AI suggestion you decided not to use, and why
Skipping complex data storage: Early on, we discussed adding a database or writing logic to read/write to a local JSON file. I decided to reject this and stick to a simple in-memory Python list. The assignment instructions explicitly allowed in-memory storage, and I wanted to prioritize keeping the codebase clean, readable, and easy for me to explain during the technical interview rather than overcomplicating it.
Rejecting standard path execution: The AI initially suggested running the server with just `uvicorn src.main:app`. On my Windows machine, this caused path errors. I decided to reject that and use `python -m uvicorn src.main:app` instead, which bypasses the Windows path issues. I made sure to update my `README.md` to reflect the most stable commands.