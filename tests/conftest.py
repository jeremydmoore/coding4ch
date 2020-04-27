# conftest.py is the config file for pytest

# access directory of
@pytest.fixture('session')
def test_data_dir_path():
    return Path(__file__).name.joinpath('test_data')
