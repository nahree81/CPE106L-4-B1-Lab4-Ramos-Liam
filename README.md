# Lab Activity 4: Design Pattern and Unit Testing

## Description

This laboratory activity demonstrates the implementation of a simple Python application using the **Strategy Design Pattern** and automated unit testing.

The application is a **Grade Calculator** that supports different grading methods:

* Average Grading
* Weighted Grading

The Strategy Design Pattern allows the grading method to be changed without modifying the main `GradeCalculator` class.

## Learning Objective

Implement a small Python application that demonstrates one simple design pattern and includes automated unit tests.

## Design Pattern Used

### Strategy Pattern

The **Strategy Pattern** was selected because the Grade Calculator can use different algorithms to calculate a student's grade.

The program defines a common `GradingStrategy` interface. Different grading methods then implement this interface:

* `AverageGradingStrategy`
* `WeightedGradingStrategy`

The `GradeCalculator` receives a grading strategy and uses it to calculate the final grade.

This design makes the application easier to extend because new grading methods can be added without changing the `GradeCalculator` class.

## Folder Structure

```text
labactivity4/
│
├── src/
│   ├── __init__.py
│   ├── grade_calculator.py
│   └── main.py
│
├── tests/
│   └── test_grade_calculator.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Requirements

* Python
* Python Virtual Environment
* Git
* GitHub
* Ubuntu WSL, if required by the laboratory instructions

No external Python packages are required because the application uses Python's built-in `unittest` framework.

## How to Run

### 1. Create the Virtual Environment

```text
python -m venv .venv
```

### 2. Activate the Virtual Environment

On Windows PowerShell:

```text
.venv\Scripts\activate
```

The terminal should display:

```text
(.venv)
```

### 3. Run the Application

```text
python src/main.py
```

The program displays two grading methods:

```text
=== Grade Calculator ===
1. Average Grading
2. Weighted Grading
```

## Grading Methods

### Average Grading

The average grading strategy calculates the arithmetic mean of all entered scores.

For example:

```text
80 90 100
```

Calculation:

```text
(80 + 90 + 100) / 3 = 90
```

Expected output:

```text
Final Grade: 90.00
```

### Weighted Grading

The weighted grading strategy uses the following weights:

```text
30% + 30% + 40%
```

For example:

```text
80 90 100
```

Calculation:

```text
80 × 0.30 = 24
90 × 0.30 = 27
100 × 0.40 = 40

24 + 27 + 40 = 91
```

Expected output:

```text
Final Grade: 91.00
```

## Automated Unit Testing

The project uses Python's built-in `unittest` framework.

Run the tests using:

```text
python -m unittest discover -s tests -v
```

The project contains three automated test cases:

1. Test average grading
2. Test weighted grading
3. Test empty scores

Expected result:

```text
Ran 3 tests

OK
```

## Test Cases

### Test Case 1: Average Grading

Input:

```text
1
80 90 100
```

Expected:

```text
Final Grade: 90.00
```

### Test Case 2: Weighted Grading

Input:

```text
2
80 90 100
```

Expected:

```text
Final Grade: 91.00
```

### Test Case 3: Empty Scores

The unit test checks that an empty list of scores returns:

```text
0
```

