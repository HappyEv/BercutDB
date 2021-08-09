import pytest
from framework.database.executor import Executor
from framework.database.connection import Connection
from file_manager import FileManager


@pytest.fixture(scope="class")
def setup(request):
    connection = Connection()
    executor = Executor(connection.conn)
    test_data = FileManager("resourses/test_data.json")
    request.cls.executor = executor
    request.cls.test_data = test_data
    yield
    connection.clear()
