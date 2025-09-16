## README_TESTS

**Overview**
   This repository contains manual (Postman) and automated (pytest) tests for the FastAPI-based User Management API. Follow the steps below to set up the environment, run the API, and execute the tests.

**Quick Start**
   2.1 Create a virtual environment & install dependencies
   python -m venv .venv

# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# If you have a requirements file:
pip install -r requirements.txt
# Otherwise (minimal for tests):
pip install -U pip pytest requests uvicorn fastapi pydantic

   2.2 Start the API locally
uvicorn main:app --reload --host 0.0.0.0 --port 8000
# Base URL: http://localhost:8000
# Docs:     http://localhost:8000/docs

   2.3 (Optional) Seed example data
python seed_data.py
# Uses BASE_URL = http://localhost:8000 by default and creates sample users.

**Automated Tests (pytest)**

Run all tests:

pytest -q test_api.py -v


Run a subset:

pytest -q -k "health or login" -v
pytest -q -k "TestUserCreation" -v


**Notes**

Some tests require a valid Bearer token. If needed, first call POST /login and pass the token to tests via environment or extend the test to log in automatically.

DELETE /users/{id} requires Basic Auth (admin credentials). PUT /users/{id} requires Bearer.

**Manual Tests (Postman)**

Create an Environment: {{baseUrl}} = http://localhost:8000
Typical flow:
POST /login → copy token
GET /users / POST /users / GET /users/{id}
PUT /users/{id} with Authorization: Bearer <token>
DELETE /users/{id} with Basic Auth (admin)
GET /health, GET /stats, GET /users/search
Save screenshots into ./screenshots/.

**Test Categories (automation & manual)**

TestUserCreation            — create user (positive/negative/boundaries)
TestUserRetrieval           — list/get user (pagination, sorting)
TestUserUpdate              — update user (auth/validation)
TestUserDeletion            — delete user (admin/basic auth, idempotency)
TestAuthentication          — login/logout/session behaviors
TestSystemEndpoints         — health/stats/root checks
TestSecurityVulnerabilities — info disclosure, rate limiting, ownership/RBAC

**Artifacts**

test_cases.md — manual test scenarios
bugs_report.md — issues found
test_report.md — final report (summary, metrics, recommendations)
test_api.py — pytest suite
screenshots/ — evidence images

**Troubleshooting**

Port in use: start on another port, e.g. uvicorn main:app --reload --port 8001
401 on protected endpoints: refresh token via POST /login, set Authorization: Bearer <token>
Rate limit expectations: /users creates may return 429 if you exceed >100 req/min per IP (by design)

**Environment**

Base URL: http://localhost:8000
Admin (example): admin_user / Admin@2024
Dynamic test user pattern: rl_<timestamp> / oldnew50