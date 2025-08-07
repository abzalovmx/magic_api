import pytest
from endpoints.create_url_endpoint import CreateUrlEndpoint
import faker, string

fc = faker.Faker()

@pytest.fixture
def url_creator_endp():
    return CreateUrlEndpoint()

@pytest.fixture
def random_string():
    return fc.text()