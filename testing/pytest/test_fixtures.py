import pytest
pytest.skip(allow_module_level=True)

@pytest.fixture
def config_dict():
    yield {"option": "value"}

def test_config(config_dict):
    my_module.run_function(config=config_dict)

def test_modifying_config(config_dict):
    config_dict["option"] = "value2"
    my_module.run_function(config=config_dict)

@pytest.fixture
def random_user():
    username = my_module.create_random_user()
    yield username
    my_module.delete_user(username)


def test_func(random_user):
    my_module.some_func(random_user)

def test_func_with_config(random_user, config_dict):
    my_module.some_func(random_user, config=config_dict)

@pytest.fixture
def random_user_with_home(random_user, tmp_path):
    home_dir = (tmp_path / random_user.username).mkdir()
    random_user.set_home_dir(home_dir)
    yield random_user

def test_get_home_dir(random_user_with_home):
    user_homedir = random_user_with_home.get_homedir()
    assert user_homedir.name == random_user_with_home.username

class User1Class:
    def test_request_1(self, query_session: Session, registered_endpoint_base: str, payload_options) -> None:
        response = query_session.get(f"{registered_endpoint_base}/query_1",
                                     data=my_module.Class1.query_payload_1(user_id, **payload_options))
        assert response.content() == EXPECTED_RESPONSE_CONTENT_1

    def test_request_2(self, query_session: Session, registered_endpoint_base: str, payload_options) -> None:
        response = query_session.get(f"{registered_endpoint_base}/query_2",
                                     data=my_module.query_payload_2(user_id, **payload_options))
        assert response.content() == EXPECTED_RESPONSE_CONTENT_2

class User2Class:
    def test_request_1(self, query_session: Session, registered_endpoint_base: str, payload_options) -> None:
        response = query_session.get(f"{get_api_url(user_id)}/query_1",
                                     data=my_module.Class2.query_payload_1(user_id, **payload_options))
        assert response.content() == EXPECTED_RESPONSE_CONTENT_1

@pytest.fixture(scope="function")
def test_request_3(query_session: Session, payload_options) -> None:
    payload_options["example"] = "value_3"
    response = session.get(f"{BASE}/example_endpoint", my_module.get_query_payload(**payload_options))
    assert response.content() == EXPECTED_RESPOSNE_3
