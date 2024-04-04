import pytest

from user import User


@pytest.fixture
def user_data():
    user = User()
    user_data = user.create_user_return_user_data()
    yield user_data
    user.delete_user(user_data[3])
