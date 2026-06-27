# Debugging, Root Cause Analysis and Unit Testing

This repository contains Python solutions for the six debugging assessment
problems. Each problem has a small implementation under `solutions/` and pytest
coverage under `tests/`. The tests use Python's built-in `unittest` module, so
no third-party test dependency is required.

## Project Layout

```text
project/
├── solutions/
├── tests/
├── README.md
└── DEBUGGING_REPORT.md
```

## Running Tests

Run the test suite:

```bash
python3 -m unittest discover -s tests
```

## Assumptions

- CSV record counts mean data rows, not the header row.
- Blank CSV rows are ignored.
- Malformed JSON should not crash callers with a raw decoder exception.
- `process_records` keeps the same output shape as the original code.
- Discounts are percentages from `0` to `100`, inclusive.
- The safer user cache is written for threaded Python services.
