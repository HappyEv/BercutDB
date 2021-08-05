import pytest
from file_manager import FileManager
from framework.executor import Executor


@pytest.fixture(scope="class")
def setup(request):
    driver = FileManager.get_data("driver", "../config.json")
    server = FileManager.get_data("server", "../config.json")
    db = FileManager.get_data("db", "../config.json")
    user = FileManager.get_data("user", "../config.json")
    password = FileManager.get_data("password", "../config.json")
    executor = Executor(driver, server, db, user, password)
    request.cls.executor = executor
    yield
    executor.clear()