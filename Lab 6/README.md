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
| `test_train_fare.py` | Original starter test cases used for baseline coverage |
| `CodeCoverageTest_PES2UG24CS586_train_fare.py` | Additional test cases for code coverage |
| `BranchCoverageTest_PES2UG24CS586_train_fare.py` | Additional test cases for branch coverage |
| `Before_CodeCoverage_PES2UG24CS586.png` | Initial code coverage result |
| `Before_BranchCoverage_PES2UG24CS586.png` | Initial branch coverage result |
| `After_CodeCoverage_PES2UG24CS586.png` | Final code coverage result |
| `After_BranchCoverage_PES2UG24CS586.png` | Final branch coverage result |

## Software Requirements

- Python 3.x
- pytest
- coverage.py

## Installation

Install the required dependencies:

```bash
pip install pytest coverage
```

## Initial Coverage (Before Adding Tests)

The starter test file, `test_train_fare.py`, contains two test cases. These tests were run first to establish the initial coverage baseline.

### Initial Code Coverage

Run the following commands from the `Lab 6` directory:

```bash
python -m coverage erase
python -m coverage run --source=train_fare -m pytest -v test_train_fare.py
python -m coverage report -m
```

Initial result: **45% code coverage**

- Tests passed: **2**
- Statements: **31**
- Missed statements: **17**
- Line coverage: **45%**

### Initial Branch Coverage

Run the following commands from the `Lab 6` directory:

```bash
python -m coverage erase
python -m coverage run --branch --source=train_fare -m pytest -v test_train_fare.py
python -m coverage report -m
```

Initial result: **40% branch coverage**

- Tests passed: **2**
- Statements: **31**
- Missed statements: **17**
- Branches: **22**
- Partial branches: **7**
- Branch coverage: **40%**

## Improved Code Coverage

Additional test cases were created to exercise the statements and conditions in `train_fare.py`.

Run the code coverage test suite from the `Lab 6` directory:

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

## Improved Branch Coverage

A separate test suite was created to exercise both outcomes of the decision branches, including boundary conditions.

Run the branch coverage test suite from the `Lab 6` directory:

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

## Before-and-After Comparison

| Metric | Before adding tests | After adding tests |
| --- | ---: | ---: |
| Starter tests passed | 2 | — |
| Code coverage | 45% | 100% |
| Branch coverage | 40% | 100% |
| Statements | 31 | 31 |
| Missed statements | 17 | 0 |
| Branches | 22 | 22 |
| Partial branches | 7 | 0 |

## Overall Test Summary

| Test suite | Tests passed | Coverage result |
| --- | ---: | --- |
| Original starter tests | 2 | 45% line coverage; 40% branch coverage |
| Code coverage tests | 18 | 100% line coverage |
| Branch coverage tests | 25 | 100% branch coverage |

The two additional test suites contain 43 successful test executions in total (18 code coverage tests and 25 branch coverage tests).

## Conclusion

The initial starter tests achieved 45% line coverage and 40% branch coverage. Additional test cases were then developed to cover the statements and decision branches in the Train Fare Calculator. The improved code coverage suite achieved 100% line coverage, and the branch coverage suite achieved 100% branch coverage, with zero missed statements and zero partial branches.
