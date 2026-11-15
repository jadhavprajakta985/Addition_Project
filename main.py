
from fastapi import FastAPI
from pydantic import BaseModel
import csv
import os

# Create FastAPI application
app = FastAPI(title="Addition Application")

# CSV file for storing input data
DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "addition_data.csv")

os.makedirs(DATA_DIR, exist_ok=True)


# Define input structure
class Numbers(BaseModel):
    num1: float
    num2: float


# Home page
@app.get("/")
def home():
    return {
        "message": "Welcome to Addition Application"
    }


# Addition API
@app.post("/add")
def add_numbers(numbers: Numbers):

    # Perform addition
    result = numbers.num1 + numbers.num2

    # Store input and output in CSV
    file_exists = os.path.exists(DATA_FILE)

    with open(DATA_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(DATA_FILE) == 0:
            writer.writerow(["num1", "num2", "result"])

        writer.writerow([
            numbers.num1,
            numbers.num2,
            result
        ])

    # Return response
    return {
        "num1": numbers.num1,
        "num2": numbers.num2,
        "result": result,
        "message": "Addition successful"
    }
