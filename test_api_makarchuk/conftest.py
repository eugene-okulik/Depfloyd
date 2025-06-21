import pytest

def pytest_configure(config):
    config.addinivalue_line("markers", "critical: marks tests as critical (run these first)")
    config.addinivalue_line("markers", "medium: marks tests as medium priority")

def pytest_collection_modifyitems(config, items):
    items.sort(key=lambda item: (
        0 if item.get_closest_marker("critical") else
        1 if item.get_closest_marker("medium") else 2
    ))

pytest.filterwarnings = [
    "ignore::urllib3.exceptions.InsecureRequestWarning",
    "ignore::DeprecationWarning",
    "ignore::PendingDeprecationWarning"
]
