# L6_L7_25_train_fare — Train Fare

## Lab 7: Fuzz Testing

### Objective

To use Python's Hypothesis library for fuzz testing, identify input validation bugs, and improve the robustness of the Train Fare application.

### Files

| File | Description |
| --- | --- |
| `train_fare.py` | Train Fare application with input validation and bug fixes |
| `test_train_fare.py` | Hypothesis-based fuzz tests for all three functions |
| `README.md` | Project documentation |

### Functions Tested

1. **`parse_pnr()`** – Validates and parses a 10-digit PNR.
2. **`journey_distance()`** – Calculates journey distance from comma-separated station distances.
3. **`berth_type()`** – Determines the berth type from coach and seat information.

### Testing Process

1. Installed `hypothesis` and `pytest`.
2. Executed the original application using valid inputs.
3. Created Hypothesis fuzz tests for all three functions.
4. Ran the tests and identified failures caused by unexpected inputs.
5. Modified the application to handle invalid inputs safely.
6. Re-ran the application and fuzz tests to verify the fixes.

### Test Results

- Original application: All three functions worked with valid sample inputs.
- Original fuzz tests: All three tests failed, exposing input validation issues.
- Fixed application: Added defensive input validation.
- Final fuzz tests: All 3 tests passed.

### Installation

```bash
pip install hypothesis pytest
```

### Execution

Run the application:

```bash
python train_fare.py
```

Run fuzz tests:

```bash
python -m pytest test_train_fare.py -v
```

### Deliverables

1. PDF report containing the required screenshots.
2. Fixed `train_fare.py` application.
3. Updated `test_train_fare.py` Hypothesis test file.

Refer to the Lab 7 Fuzz Testing Student Handout for the original instructions.
