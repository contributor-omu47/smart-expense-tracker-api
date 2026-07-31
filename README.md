# Smart Expense Tracker API

A RESTful API to manage personal expenses, built with Python and FastAPI.

## Features
* **CRUD Operations**: Add, view, filter, and delete expenses.
* **Totals Calculation**: Calculate total expenses overall or filtered by category.
* **Data Validation**: Automated request validation using Pydantic.
* **Interactive Docs**: Automatically generated Swagger/OpenAPI documentation.
* **Storage**: In-memory data structures (as permitted by the requirements) for zero-dependency local execution.

---

## Prerequisites
* Python 3.8 or higher installed on your system.

## 1. Installation

First, clone this repository and navigate into the project directory. Then, set up a virtual environment and install the dependencies.

**For Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt