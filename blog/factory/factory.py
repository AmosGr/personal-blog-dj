from factory import Faker,LazyAttribute,SubFactory
from faker import Factory as FakerFactory
from factory.django import DjangoModelFactory

from django.contrib.auth.models import User
from django.utils.timezone import now

from ..models.post import Post

faker = FakerFactory.create()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
    
    email = Faker('safe_email')
    username = LazyAttribute(lambda x: faker.name())

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop("password",None) 
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()
        return user


class PostFactory(DjangoModelFactory):
    title = LazyAttribute(lambda x: faker.sentence())
    created_on = LazyAttribute(lambda x: now())
    author = SubFactory(UserFactory)
    status = 0

    class Meta: 
        model = Post