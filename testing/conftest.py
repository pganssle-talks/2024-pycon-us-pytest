def pytest_configure(config):
    config.addinivalue_line(
        "markers", "heavy: slow tests"
    )
