import pytest


class MockClient:
    """Mock client that dynamically returns a success dictionary for any called API."""

    def __getattr__(self, name):
        def method(*args, **kwargs):
            return {"status": "success", "called": name, "args": args, "kwargs": kwargs}

        return method


@pytest.fixture
def mock_client():
    """Provides a dynamic mock client for owncast API actions."""
    return MockClient()
