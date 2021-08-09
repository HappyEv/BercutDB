import pytest
from framework.database.executor import Executor
from framework.database.connection import Connection


@pytest.fixture(scope="class")
def setup(request):
    connection = Connection()
    executor = Executor(connection.conn)
    request.cls.executor = executor
    yield
    connection.clear()