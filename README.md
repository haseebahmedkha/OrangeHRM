# OrangeHRM UI Automation Tests

A PyTest + Selenium UI automation suite for OrangeHRM using the Page Object Model (POM). Tests are configuration-driven and include logging utilities to make test execution and debugging straightforward.

## Repository Structure
- `tests/` — PyTest test modules (e.g. `tests/test_search_user.py`)
- `pages/` — Page object classes (e.g. `login_Page.py`, `adminPage.py`, `adminPage_Search.py`)
- `Utilities/` — Helpers and logger (e.g. `logger.py`)
- `config/` — Configuration files (e.g. `config.ini`)
- `drivers/` — (optional) browser driver executables
- `conftest.py` — fixtures (provides the `setup` fixture returning a WebDriver)
- `requirements.txt` — Python dependencies (if present)

## Key Features
- PyTest test runner with test classes and fixtures
- Page Object Model for maintainable UI interactions
- Centralized configuration (`config/config.ini`)
- Simple logging via `Utilities/logger.py`
- Example test: `tests/test_search_user.py` (search admin user flow)

## Requirements
- Windows 10/11
- Python 3.8+
- pip
- Browser (Chrome/Edge/Firefox) and matching WebDriver (ChromeDriver, msedgedriver, geckodriver)
- Recommended packages: `pytest`, `selenium`, other dependencies in `requirements.txt`

## Setup (Windows)
1. Clone the repo:
   - `git clone https://github.com/haseebahmedkha/OrangeHRM.git`
2. Create and activate a virtual environment:
   - `python -m venv .venv`
   - `.venv\Scripts\activate`
3. Install dependencies:
   - `pip install -r requirements.txt`
   - or at minimum: `pip install pytest selenium`
4. Place the matching WebDriver executable in your `PATH` or `drivers/` folder.

## Configuration
Edit `config/config.ini` to set:
- `username` — test account username
- `password` — test account password
- (optionally) `base_url` — application URL

Example `config/config.ini` keys live under the `DEFAULT` section.

## Running Tests
- Run all tests:
  - `pytest -q`
- Run a specific test:
  - `pytest tests/test_search_user.py::TestSearchUser_name::test_search_by_username -q`
- Run in PyCharm:
  - Create a pytest run configuration or right-click the test file/class and choose Run.

Notes:
- Tests rely on a `setup` fixture (in `conftest.py`) that initializes and returns a WebDriver instance.
- Many tests use implicit `time.sleep()` calls; consider adding explicit waits for stability.

## Test Design & Conventions
- Tests use the Page Object Model: methods on page classes encapsulate UI actions.
- Tests log actions via `Utilities/logger.py` for traceability.
- Keep tests independent and deterministic where possible.

## Troubleshooting
- "Element not found" or flaky tests: ensure the correct WebDriver version and increase waits or convert to explicit waits.
- Authentication failure: verify credentials in `config/config.ini`.
- Browser not launching: confirm WebDriver path and permissions.

## Contributing
- Open issues or submit PRs with clear descriptions.
- Follow PEP8 and add/update tests for new features or fixes.

## License
- Add your project license here (e.g., MIT). If no license is provided, assume repository-specific terms.

## Contact
- Repo owner: `haseebahmedkha` (GitHub)
