# Python Basic Calculator

A basic calculator built in Python that performs the four basic arithmetic operations.

## Features
- Addition
- Subtraction
- Multiplication
- Division (with error handling for division by zero)

## Project Structure

The project is divided into two main modules to separate business logic from the user interface:
- `logica.py`: Contains the core mathematical functions.
- `calculator.py`: The main script that handles user input and output.

## How to use

1. Make sure you have Python 3 installed.
2. Run the `calculator.py` file in your terminal or IDE.
3. Follow the on-screen instructions to perform calculations.

## Testing

This project uses `pytest` to ensure the logic works correctly across different scenarios (positive numbers, negative numbers, mixed signs, and zero). 

## Technologies

- Python 3

- Pytest (Testing Framework)

## Author

Daniel Ferreiro


To run the tests, first install the dependencies. Then, run the test suite:

```bash
pip install pytest pytest-cov

pytest -v
To check the test coverage of the logic module:

pytest --cov=logica

