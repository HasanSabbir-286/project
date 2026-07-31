# Calculator with History 🧮

A command-line calculator built with Python that performs basic arithmetic operations and stores calculation history in a JSON file. The history is saved permanently, so it is available even after closing and reopening the program.

## Features

- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division
- 📜 View calculation history
- 🗑️ Clear calculation history
- 💾 Automatic history saving using JSON
- ✅ Input validation for numbers
- ✅ Menu input validation
- ✅ Confirmation before clearing history
- ⚠️ Prevents division by zero

## Technologies Used

- Python 3
- JSON (for data storage)
- File Handling
- Functions
- Loops
- Exception Handling (`try` / `except`)

## Project Structure

```
Calculator/
│── calculator.py
│── calc_history.json
└── README.md
```

## How to Run

1. Clone the repository:

```bash
git clone <your-repository-link>
```

2. Navigate to the project folder:

```bash
cd Calculator
```

3. Run the program:

```bash
python calculator.py
```

## Menu

```
======= Calculator =======

1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. View History
6. Clear History
7. Exit
```

## Example

```
======= Calculator =======

Choose an option: 1

Enter First Number: 10

Enter Second Number: 20

10.0 + 20.0 = 30.00
```

### History

```
======= Calculator History =======

10.0 + 20.0 = 30.00
50.0 - 15.0 = 35.00
12.0 * 5.0 = 60.00
```

## Data Storage

All calculations are stored in the `calc_history.json` file.

Example:

```json
{
    "calc_history": [
        "10.0 + 20.0 = 30.00",
        "50.0 - 15.0 = 35.00"
    ]
}
```

## Skills Practiced

- Python functions
- User input validation
- Exception handling
- JSON file handling
- Reading and writing files
- Loops
- Lists
- Program organization
- Basic data persistence

## Future Improvements

- Scientific calculator functions
- Percentage calculations
- Square root and power operations
- Delete a single history entry
- GUI version using Tkinter
- Calculation timestamps

## Author

**Hasan Sabbir**

This project was created as part of my Python learning journey.