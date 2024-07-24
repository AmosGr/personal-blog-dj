# conftest.py

import pytest
from blog.factory.factory import UserFactory, PostFactory

@pytest.fixture
def user(db):
    return UserFactory.create(password='12345')

@pytest.fixture
def post(user):
    return PostFactory.create(author=user)
