Data Validation & Models

AI Generated: I used the AI to generate the Pydantic models (ExpenseCreate and Expense) to handle data validation.

Validation/Changes: I reviewed the models to ensure they map exactly to the assignment requirements (id, title, amount, category, date). I decided to use Python's built-in date type for strict date validation rather than a simple string, and split the models into create/read representations to handle ID generation securely on the backend.