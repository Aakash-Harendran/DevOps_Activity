# DevOps Activity: Advanced GitHub Actions for a Flask Application

## Overview
This project implements a minimal Flask API and integrates advanced GitHub Actions workflows for CI, linting, code coverage, security scanning, and dependency management.

---

## Endpoints Implemented
- **GET /hello**  
  Returns a simple JSON message: `{"message": "Hello, World!"}`

- **POST /echo**  
  Accepts JSON payload and returns the same payload with status code `201`.

- **PUT /echo**  
  Accepts JSON payload and updates server-side data (for demonstration), returns the updated payload with status code `200`.

- **DELETE /echo**  
  Accepts JSON payload and removes server-side data (for demonstration), returns status code `204`.

---

## Tests
- **`test_app.py`** contains unit tests for all endpoints using `pytest`.
- Run locally with:

```bash
pytest -q
