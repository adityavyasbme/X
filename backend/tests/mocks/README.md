# Mocks

## Description

Store mock or stub implementations used in your tests in this directory.

## Types of Tests 

Mocks and stubs for isolating components during testing.

## Example

 Create mock objects or stubs for external dependencies (e.g., databases, APIs) to isolate the code under test and control its behavior.

**Directory Structure** 

```bash
project_root/
├── app.py
├── tests/
│ ├── mocks/
│ │ ├── mock_database.py
│ │ ├── mock_api.py
│ │ └── ...
│ ├── ...
```