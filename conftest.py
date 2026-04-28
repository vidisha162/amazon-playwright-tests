import pytest

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "parallel: mark test to run in parallel"
    )