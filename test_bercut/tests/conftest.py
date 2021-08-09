import pytest
from framework.database.executor import Executor
from framework.database.connection import Connection
from framework.database.file_manager import FileManager


@pytest.fixture(scope="class")
def setup(request):
    connection = Connection()
    executor = Executor(connection.conn)
    test_data = FileManager("resourses/test_data.json")
    post_delete = []
    request.cls.executor = executor
    request.cls.test_data = test_data
    request.cls.post_delete = post_delete
    yield
    for i in reversed(request.cls.post_delete):
        i.del_from_table(request.cls.executor)
    connection.clear()
    executor.clear()
    test_data.clear()
