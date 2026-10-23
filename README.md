# DVLA-Coding-Assessment-Part-1
Python implementation and pytest tests for the DVLA coding assessment

## Overview

This project implements the vehicle registration lookup functionality for Part 1 of the DVLA SDET coding assessment.

The solution is developed in Python and uses a JSON file to store vehicle registration details. 
## Features
1. **Count vehicle registrations** – Returns the total number of vehicle registration records.
2. **Retrieve vehicle details** – Searches for a given registration number
3. **Handle missing data** – Returns `None` for the Vehicle ID when it is not available 

## Project Structure

```text
DVLACodingAssessmentPart_01/
├── dvla_demo_part1.py
├── Vehicles_reg_details.json
├── test_unittest_vehiclesreg_details.py
├── testdata_dvla.txt
├── .gitignore
└── README.md
```

## Technologies Used

- Python
- JSON
- pytest
- pytest-html (for HTML test reports)

## Prerequisites

- Python 3
- pytest
- pytest-html

Install the testing dependencies using:

```bash
pip install pytest pytest-html
```

## How to Run

Run the automated tests from the project root directory:

```bash
pytest .\test_unittest_vehiclesreg_details.py -s
```

To generate an HTML test report:

```bash
pytest .\test_unittest_vehiclesreg_details.py -s --html=report.html
```

## Test Coverage

The automated tests cover:

- Total vehicle registration count.
- Retrieval of vehicle details for valid registration numbers.
- Handling of a registration with no Vehicle ID.
- Handling of an unknown registration number.

## Test Results

All three automated tests passed successfully in the local test run.

## Data Source

Vehicle registration records are stored in `Vehicles_reg_details.json`. The application reads the JSON data at runtime;
no database or external API is required.