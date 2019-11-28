from pytest import fixture
from distutils import dir_util
import os


@fixture
def datadir(tmp_path, request):
    """
    Moves all contents of the folder with the same name as the test module to a
    temporary directory, so the tests can use it.
    """
    filename = request.module.__file__
    test_dir, _ = os.path.splitext(filename)

    if os.path.isdir(test_dir):
        dir_util.copy_tree(test_dir, str(tmp_path))

    return tmp_path
