import pytest
from faker import Faker
from lab12.users import UserRegistry
@pytest.fixture
def registry():
    store=UserRegistry()
    yield store
    store.clear()
    assert store.all()==[]
    if hasattr(store,'close'):store.close()
@pytest.fixture
def seeded(registry):
    registry.add('Анна Смирнова',25,'anna@example.com')
    registry.add('Олег Иванов',40,'oleg@example.com')
    return registry
@pytest.fixture
def datasets():
    fake=Faker('ru_RU');fake.seed_instance(319)
    return [dict(name=fake.first_name()+' '+fake.last_name(),age=fake.random_int(1,100),email=f'member{i}@example.com') for i in range(75)]
