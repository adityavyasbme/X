# Data Driven Tests

## Description

The "data" directory is used for test data or data-driven tests.

## Types of Tests 

Data-driven tests that use external data sources.

## Example

Store test data files (e.g., JSON, CSV) in this directory and write tests that use this data to ensure different data scenarios are covered.

**Directory Structure** 

```bash
project_root/
├── app.py
├── tests/
│ ├── data/
│ │ ├── test_data_1.json
│ │ ├── test_data_2.csv
│ │ └── ...
│ ├── ...
```