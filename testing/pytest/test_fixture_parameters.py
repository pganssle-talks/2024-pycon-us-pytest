import pytest
import dataclasses
import functools
import random
import string
import uuid

from typing import MutableMapping

@dataclasses.dataclass
class User:
    base: str | None = None

    @functools.cached_property
    def username(self) -> str:
        username = self.base or ""
        if not username:
            username = "".join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 8)))
        username += f"{random.randint(0, 1_000_000):04d}"
        return username

    @functools.cached_property
    def uid(self) -> str:
        return str(uuid.uuid4())

    def create_user(self):
        _USERS[self.username] = self

    def delete_user(self):
        del _USERS[self.username]

def get_user(username: str) -> User:
    return _USERS[username]

_USERS : MutableMapping[str, User]= {}

@pytest.fixture
def username_base() -> str | None:
    return None

@pytest.fixture
def random_user(username_base: str | None) -> str:
    user = User(username_base)
    user.create_user()
    yield user.username
    user.delete_user()

@pytest.mark.parametrize("username_base", ["josé"])
def test_users_with_accents(random_user : str) -> None:
    assert get_user(random_user).base == "josé"

@pytest.fixture
def random_user_indirect(request) -> str:
    username_base = request.param
    user = User(username_base)
    user.create_user()
    yield user.username
    user.delete_user()


def test_users(random_user):
    assert get_user(random_user).base is None

@pytest.mark.parametrize("random_user_indirect", ["josé"], indirect=True)
def test_users_with_accents_indirect(random_user_indirect):
    assert get_user(random_user_indirect).base == "josé"


