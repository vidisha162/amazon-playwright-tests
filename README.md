# Amazon Automation Tests — Playwright Python

# 🧪 Amazon Automation Test Suite (Playwright + Python)

Automated end-to-end test suite for Amazon.com built using **Playwright with Python and Pytest**.

It validates product search, cart functionality, and price extraction for two test scenarios, executed in parallel using pytest-xdist.

---

## 📋 Test Scenarios

| Test Case | Description |
|----------|-------------|
| TC1 | Search iPhone → Add to cart → Extract and print price |
| TC2 | Search Samsung Galaxy → Add to cart → Extract and print price |

✔ Both test cases execute in parallel using pytest-xdist (-n 2)

---

## 🛠️ Tech Stack

- **Language:** Python 3.13  
- **Automation Framework:** Playwright  
- **Test Framework:** Pytest  
- **Parallel Execution:** pytest-xdist  
- **Browser:** Chromium  

---

## ⚙️ Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/vidisha162/amazon-playwright-tests.git
cd amazon-playwright-tests

#Create Virtual Environment
python -m venv .venv

# Windows
.venv\Scripts\activate


Install Dependencies
pip install playwright pytest pytest-playwright pytest-xdist


Install Browser
playwright install chromium
▶️ Running Tests
Run tests sequentially
pytest tests/test_amazon.py -v -s --headed
Run tests in parallel (recommended)
pytest tests/test_amazon.py -v -s -n 2
Run individual test cases
# TC1
pytest tests/test_amazon.py::test_iphone_search_and_cart -v -s --headed

# TC2
pytest tests/test_amazon.py::test_galaxy_search_and_cart -v -s --headed
Run in headless mode
pytest tests/test_amazon.py -v -s -n 2 --headless
📊 Sample Output
TEST CASE 1: iPhone Search
📱 Product : iPhone
💰 Price : INR 1,21,424.88

TEST CASE 2: Samsung Galaxy Search
📱 Product : Samsung Galaxy
💰 Price : INR 81,892.16

2 passed in 73.53s
📁 Project Structure
amazon-playwright-tests/
│
├── tests/
│   └── test_amazon.py        # Main test cases (TC1 & TC2)
│
├── conftest.py               # Pytest fixtures
├── pytest.ini               # Parallel execution config
├── requirements.txt          # Dependencies
└── README.md
🔄 Parallel Execution Design

This project uses pytest-xdist for parallel execution.

pytest -n 2

Execution flow:

Worker 1 → TC1 (iPhone test)
Worker 2 → TC2 (Samsung Galaxy test)

Each worker runs an independent browser instance, enabling faster execution.

🚀 Key Highlights
Robust locator strategy with fallback selectors
Dynamic price extraction handling multiple UI variations
Parallel execution for performance optimization
Real-world e-commerce automation scenario

---

# 💡 WHY THIS VERSION IS BETTER

✔ cleaner formatting  
✔ more “engineering style”  
✔ better recruiter readability  
✔ highlights **key skills (very important)**  
✔ looks like real QA/DevOps project, not assignment dump  

---

# ⚡ FINAL ADVICE BEFORE YOU SEND

You are now at this level:

👉 “Hireable internship submission”

Just make sure:
- GitHub link works
- repo is public
- tests pass again before sending

---
