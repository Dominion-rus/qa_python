import pytest
from main import BooksCollector


@pytest.fixture()
def new_collector():
    collector = BooksCollector()
    return collector
