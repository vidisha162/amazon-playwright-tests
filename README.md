# Amazon Automation Tests — Playwright Python

Automated test suite for Amazon.com built with **Playwright + Python**.  
Covers iPhone and Samsung Galaxy search, cart addition, and price extraction — with **parallel execution**.

---

## 📋 Test Cases

| Test | Description |
|------|-------------|
| TC1 | Search for iPhone → Add to cart → Print price to console |
| TC2 | Search for Samsung Galaxy → Add to cart → Print price to console |

Both test cases run in **parallel** using `pytest-xdist`.

---

## 🛠️ Tech Stack

- **Language:** Python 3.13
- **Framework:** Playwright + pytest
- **Parallel Execution:** pytest-xdist (`-n 2`)
- **Browser:** Chromium

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.10+
- pip

### 1. Clone the repository
```bash
git clone https://github.com/vidisha162/amazon-playwright-tests.git
cd amazon-playwright-tests
```

### 2. Create virtual environment
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install playwright pytest-playwright pytest-xdist
```

### 4. Install Chromium browser
```bash
playwright install chromium
```

---

## ▶️ Running Tests

### Run both tests sequentially
```bash
pytest tests/test_amazon.py -v -s --headed
```

### Run both tests in PARALLEL (2 workers)
```bash
pytest tests/test_amazon.py -v -s -n 2
```

### Run specific test
```bash
# iPhone only
pytest tests/test_amazon.py::test_iphone_search_and_cart -v -s --headed

# Samsung Galaxy only
pytest tests/test_amazon.py::test_galaxy_search_and_cart -v -s --headed
```

### Run headless (no browser UI)
```bash
pytest tests/test_amazon.py -v -s -n 2 --headless
```

---

## 📊 Expected Output

TEST CASE 1: iPhone Search
──────────────────────────────────────────
📱  Product : iPhone
💰  Price   : INR 1,21,424.88
──────────────────────────────────────────
TEST CASE 2: Samsung Galaxy Search
──────────────────────────────────────────
📱  Product : Samsung Galaxy
💰  Price   : INR 81,892.16
──────────────────────────────────────────
2 passed in 73.53s

---

## 📁 Project Structure
amazon-playwright-tests/
├── tests/
│   └── test_amazon.py      # Main test file (TC1 + TC2)
├── conftest.py              # Pytest configuration
├── pytest.ini               # Pytest settings + parallel config
├── requirements.txt         # Dependencies
└── README.md               # This file

---

## 🔄 Parallel Execution

Tests run in parallel using `pytest-xdist` with 2 workers:

```bash
pytest tests/test_amazon.py -n 2
```

- **Worker 1** → Runs TC1 (iPhone)
- **Worker 2** → Runs TC2 (Samsung Galaxy)

Both workers spawn independent browser instances simultaneously.

---
