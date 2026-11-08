# Nova Poshta UI Test Automation (`AutomatedTestingNP`)

[![Nova Poshta UI Tests](https://github.com/oleksandrmyhydiuk/AutomatedTestingNP/actions/workflows/main.yml/badge.svg)](https://github.com/oleksandrmyhydiuk/AutomatedTestingNP/actions/workflows/main.yml)
![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-4.19.0-43B02A?logo=selenium&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-8.1.1-0A9EDC?logo=pytest&logoColor=white)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Automated End-to-End (E2E) UI testing suite for the [Nova Poshta](https://novaposhta.ua/) web platform, built with **Python**, **Selenium WebDriver 4**, and **Pytest** following the **Page Object Model (POM)** design pattern.

---

## Key Features

- **Page Object Model (POM) Architecture:** Clean separation between page locators/interactions (`pages/`) and test assertions (`tests/`).
- **Resilient Element Interaction:** Built-in explicit waits (`WebDriverWait`), automatic retry logic for `StaleElementReferenceException`, JavaScript click fallbacks, and multi-locator fallback strategies to handle dynamic DOM updates on `novaposhta.ua`.
- **Zero-Config WebDriver Management:** Uses native **Selenium Manager** (Selenium 4.19) with headless Chrome (`--headless=new`) for reliable local and CI execution without external driver binaries.
- **Automated HTML Reporting & CI/CD:** Integrated with **GitHub Actions** and `pytest-html` to generate self-contained HTML test reports on every run and automatically publish them to **GitHub Pages**.

---

## Tech Stack

| Tool / Library | Version | Purpose |
| :--- | :--- | :--- |
| **Python** | `3.11+` | Core programming language |
| **Selenium WebDriver** | `4.19.0` | Browser automation & native driver management |
| **Pytest** | `8.1.1` | Test runner, fixtures, and assertions |
| **Pytest-HTML** | `4.1.1` | Self-contained HTML test report generation |
| **GitHub Actions** | `v4 / v5` | Continuous Integration & GitHub Pages deployment |

---

## Project Architecture

```text
AutomatedTestingNP/
├── .github/
│   └── workflows/
│       └── main.yml          # CI/CD pipeline (runs Pytest & deploys HTML report to GitHub Pages)
├── pages/                    # Page Object Model (POM) classes
│   ├── __init__.py
│   ├── base_page.py          # Base class (explicit waits, clear_and_type, StaleElement retry click)
│   ├── branches_page.py      # Branches search page object with resilient fallback navigation
│   ├── home_page.py          # Home page object (parcel tracking input & header menu navigation)
│   └── tracking_page.py      # Parcel tracking results & error message page object
├── tests/                    # End-to-End UI test suites
│   ├── __init__.py
│   ├── conftest.py           # Pytest WebDriver fixture (headless Chrome configuration)
│   ├── test_branches.py      # Branch & city lookup test scenarios
│   └── test_tracking.py      # Parcel tracking (EN) validation test scenarios
├── .gitignore                # Git ignore rules for Python environments and generated reports
├── LICENSE                   # MIT License
├── pytest.ini                # Pytest configuration and default CLI flags
├── README.md                 # Project documentation
├── requirements.txt          # Pinned Python dependencies
└── SECURITY.md               # Security policy and vulnerability reporting guidelines
```

---

## Implemented Test Scenarios

All tests are designed to handle dynamic UI states and markup updates gracefully.

### 1. Parcel Tracking Module (`tests/test_tracking.py`)
- **Valid Tracking Number Search (`test_valid_tracking_number`):**
  Opens the home page, submits a 14-digit express waybill number (`20450000000000`), and verifies that the tracking page returns a non-empty parcel status or result state.
- **Invalid Tracking Number Search (`test_invalid_tracking_number`):**
  Submits a non-existent tracking number (`00000000000000`) and validates that the "not found" error message (`"Не знайдено..."`) is displayed.
- **Empty Tracking Input Handling (`test_empty_tracking_field`):**
  Attempts to trigger a search with an empty string (`""`) and verifies that the application performs an early return without navigating away from the home page URL.

### 2. Branches Search Module (`tests/test_branches.py`)
- **Existing Branch Lookup (`test_existing_branch_search`):**
  Navigates to the branches section via the header menu (with homepage fallback), selects `"Київ"` (Kyiv), searches for branch `"1"`, and verifies that the returned branch count is greater than `0`.
- **Non-Existent Branch Lookup (`test_nonexistent_branch_search`):**
  Selects `"Київ"` (Kyiv), searches for a non-existent branch number (`"99999"`), and asserts that `0` branch items are returned alongside a non-empty "no results found" message.

---

## Getting Started

### Prerequisites

- **Python 3.11+** installed on your machine
- **Google Chrome** browser installed (Selenium Manager automatically resolves the matching `chromedriver`)
- **Git**

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/oleksandrmyhydiuk/AutomatedTestingNP.git
   cd AutomatedTestingNP
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv

   # Windows (PowerShell / CMD)
   venv\Scripts\activate

   # Linux / macOS
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Running Tests

- **Run the entire test suite:**
  ```bash
  pytest
  ```

- **Run a specific test module:**
  ```bash
  pytest tests/test_tracking.py
  pytest tests/test_branches.py
  ```

- **Run tests and generate a self-contained HTML report:**
  ```bash
  pytest --html=reports/index.html --self-contained-html
  ```
  After execution, open `reports/index.html` in any browser to inspect detailed test results, durations, and logs.

---

## CI/CD Pipeline

The repository includes an automated GitHub Actions workflow (`.github/workflows/main.yml`) that runs on:
- Every `push` and `pull_request` to the `main` branch
- Manual triggers via `workflow_dispatch`

**Pipeline stages:**
1. Checks out the repository and configures Python `3.11` with `pip` dependency caching.
2. Installs pinned dependencies from `requirements.txt`.
3. Executes the Pytest suite in headless Chrome and generates `reports/index.html`.
4. Uploads the HTML report as a downloadable workflow artifact (`pytest-html-report`).
5. Deploys the latest HTML report to **GitHub Pages** on pushes to `main`.

---

## Security & License

- Please review our [Security Policy (`SECURITY.md`)](SECURITY.md) for reporting vulnerabilities and security best practices.
- Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for full details.
