# L6_L7_25_train_fare — Train Fare Calculator

## Lab 6: Code and Branch Coverage Analysis

## About

This project implements a Train Fare Calculator using Python. It calculates base train fares based on travel class and distance, applies passenger age concessions, and calculates additional Tatkal booking charges.

This lab focuses on analyzing and improving software test coverage using **pytest** and **coverage.py**.

## Application Features

- Calculate base fares for different train classes (SL, 3A, 2A, 1A).
- Validate travel class and journey distance.
- Apply age-based passenger concessions.
- Calculate Tatkal charges with minimum and maximum limits.

## Project Structure

| File | Description |
| --- | --- |
| `train_fare.py` | Original Train Fare Calculator application |
| `test_train_fare.py` | Starter test cases |
| `CodeCoverageTest_PES2UG24CS586_train_fare.py` | Additional test cases for code coverage |
| `BranchCoverageTest_PES2UG24CS586_train_fare.py` | Additional test cases for branch coverage |
| `CodeCoverage_PES2UG24CS586.png` | Code coverage terminal screenshot |
| `BranchCoverage_PES2UG24CS586.png` | Branch coverage terminal screenshot |

## Software Requirements

- Python 3.x
- pytest
- coverage.py

## Installation

Install the required dependencies:

```bash
pip install pytest coverage
```

## Code Coverage Analysis

Run the code coverage test cases from the `Lab 6` directory:

```bash
python -m coverage erase
python -m coverage run --source=train_fare -m pytest -v CodeCoverageTest_PES2UG24CS586_train_fare.py
python -m coverage report -m
```

### Result: 100% Code Coverage

- Tests passed: **18**
- Statements: **31**
- Missed statements: **0**
- Line coverage: **100%**

## Branch Coverage Analysis

Run the branch coverage test cases from the `Lab 6` directory:

```bash
python -m coverage erase
python -m coverage run --branch --source=train_fare -m pytest -v BranchCoverageTest_PES2UG24CS586_train_fare.py
python -m coverage report -m
```

### Result: 100% Branch Coverage

- Tests passed: **25**
- Statements: **31**
- Missed statements: **0**
- Branches: **22**
- Partial branches: **0**
- Branch coverage: **100%**

## Overall Test Summary

| Analysis | Tests Passed | Coverage Result |
| --- | ---: | ---: |
| Code coverage | 18 | 100% line coverage |
| Branch coverage | 25 | 100% branch coverage |
| **Total test executions** | **43** | **100% line and branch coverage** |

## Conclusion

The Train Fare Calculator was tested using separate code coverage and branch coverage test suites. All 18 code coverage tests and all 25 branch coverage tests passed. The final reports show 100% line coverage and 100% branch coverage, with no missed statements or partial branches.
