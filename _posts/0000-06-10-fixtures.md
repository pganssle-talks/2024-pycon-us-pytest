<img id="splash" class="splash"
     src="images/memes/morpheus_modular_tests.jpg"
     alt="Morpheus from the Matrix image macro with the text 'What if I told you you could have modular, composable test code without mix-ins'"
     >

--

# Fixtures

<div class="fragment fade-out disappearing-fragment nospace-fragment" data-fragment-index="0">

```python
@pytest.fixture               # Decorator to make a function a fixture
def fixture_name():
    do_some_setup()           # This code is executed before each test that uses
                              # the fixture is called
    yield fixture_payload     # This is passed to the test function

    do_some_teardown()        # This code is executed after the test function
                              # completes
```
</div>

<div class="fragment fade-in disappearing-fragment nospace-fragment" data-fragment-index="0">

```python
@pytest.fixture
def config_dict():
    yield {"option": "value"}

def test_config(config_dict):                      # config_dict() executed
    my_module.run_function(config=config_dict)

def test_modifying_config(config_dict):            # A new dict is created here
    config_dict["option"] = "value2"
    my_module.run_function(config=config_dict)

def test_hard_drive_deleted():                     # config_dict() not executed
    my_module.delete_user_hard_drive()
    assert not any(pathlib.Path("/").iterdir())
```
</div>

--

# Fixtures are modular

```python
@pytest.fixture
def random_user():
    username = my_module.create_random_user()
    yield username
    my_module.delete_user(username)

def test_func(random_user):
    my_module.some_func(random_user)

def test_func_with_config(random_user, config_dict):
    my_module.some_func(random_user, config=config_dict)

```

--

# Fixtures are composable

```python
@pytest.fixture
def random_user():
    username = my_module.create_random_user()
    yield username
    my_module.delete_user(username)

@pytest.fixture
def random_user_with_home(random_user, tmp_path):
    home_dir = (tmp_path / random_user.username).mkdir()
    random_user.set_home_dir(home_dir)
    yield random_user

def test_get_home_dir(random_user_with_home):
    user_homedir = random_user_with_home.get_homedir()
    assert user_homedir.name == random_user_with_home.username
```

--

<!-- .slide: data-visibility="hidden" -->

# Fixture scope

```python
@pytest.fixture(scope="session")
def query_session() -> Session:
    session = create_session()
    with Semaphore(4):   # No more than 4 threads a time making queries
        yield session


@pytest.fixture(scope="class")
def registered_endpoint_base(query_session: Session) -> str:
    user_id = str(uuid.uuid4())
    query_session.post(f"{BASE}/register_uuid", data={"user_id": user_id})
    yield f"{BASE}/user_id/"

@pytest.fixture(scope="function")
def payload_options():
    yield {"option_1": "value_1", "option_2": "value_2"}

```

<br/>

```python
class User1Class:
    def test_request_1(self, query_session: Session, registered_endpoint_base: str, payload_options) -> None:
        response = query_session.get(f"{registered_endpoint_base}/query_1",
                                     data=my_module.Class1.query_payload_1(**payload_options))
        assert response.content() == EXPECTED_RESPONSE_CONTENT_1

    def test_request_2(self, query_session: Session, registered_endpoint_base: str, payload_options) -> None:
        response = query_session.get(f"{registered_endpoint_base}/query_2",
                                     data=my_module.query_payload_2(**payload_options))
        assert response.content() == EXPECTED_RESPONSE_CONTENT_2
```
<!-- .element class="disappearing-fragment fragment nospace-fragment fade-out" data-fragment-index="0" -->

```python
class User2Class:
    def test_request_1(self, query_session: Session, registered_endpoint_base: str, payload_options) -> None:
        response = query_session.get(f"{get_api_url(user_id)}/query_1",
                                     data=my_module.Class2.query_payload_1(**payload_options))
        assert response.content() == EXPECTED_RESPONSE_CONTENT_1

```
<!-- .element class="disappearing-fragment fragment nospace-fragment fade-in-and-out" data-fragment-index="0" -->

```python
def test_request_3(query_session: Session, payload_options) -> None:
    payload_options["example"] = "value_3"
    response = session.get(f"{BASE}/example_endpoint", my_module.get_query_payload(**payload_options))
    assert response.content() == EXPECTED_RESPONSE_3
```
<!-- .element class="fragment nospace-fragment fade-in" data-fragment-index="1" -->

<br/>

<div class="fragment disappearing-fragment nospace-fragment fade-in-and-out" data-fragment-index="2">

- `query_session`: Run 1 time
- `registered_endpoint_base`: Run 2 times
- `payload_options`: Run 4 times

</div>

<div class="fragment fade-in" data-fragment-index="3">

<u>Available scopes:</u>

<div class="side-by-side">

<div class="left">

- `session`
- `package`
- `module`

</div>
<div class="right">

- `class`
- `function`
- *Dynamic*

</div>
</div>

</div>

Notes:

--

# Fixture UI: Parameterizing fixtures

```python
@pytest.fixture
def random_user_indirect(request) -> str:
    username_base = request.param
    user = User(username_base)
    user.create_user()
    yield user.username
    user.delete_user()


# Pass value via indirect parameterization
@pytest.mark.parametrize("random_user_indirect", ["josé"], indirect=True)
def test_users_with_accents_indirect(random_user_indirect):
    assert get_user(random_user_indirect).base == "josé"

```

<br/><br/>

```python
@pytest.fixture
def username_base() -> str | None:
    return None
```
<!-- .element class="fragment nospace-fragment fade-in" -->

```python
@pytest.fixture
def random_user(username_base: str | None) -> str:
    user = User(username_base)
    user.create_user()
    yield user.username
    user.delete_user()


# Pass value via direct parameterization (note username_base != random_user)
@pytest.mark.parametrize("username_base", ["josé"])
def test_users_with_accents(random_user):
    random_user.do_something()
```

<span class="footnote">

More on [direct parameterization](https://docs.pytest.org/en/7.2.x/how-to/fixtures.html#override-a-fixture-with-direct-test-parametrization) and [indirect parameterization](https://docs.pytest.org/en/latest/example/parametrize.html#indirect-parametrization) in the `pytest` documentation
</span>

--

# Fixture UI Issues

<pre class="code-wrapper"><tt class="hljs">$ pytest test_confusing_error_message.py 
<span class="pytest-ok">============================= test session starts ==============================</span>
<span class="pytest-ok">collected 1 item                                                               </span>

test_confusing_error_message.py <span class="pytest-bad">E                                        [100%]</span>

==================================== ERRORS ====================================
<font color="#EF2929"><span class="pytest-ok">______________________ ERROR at setup of test_refactored _______________________</span></font>
file test_confusing_error_message.py, line 1
  def test_refactored(self):
<span class="pytest-bad">E       fixture 'self' not found</span>
<span class="pytest-bad">>       available fixtures: cache, capfd, capfdbinary,
                          caplog, capsys, capsysbinary, cov, doctest_namespace,
                          monkeypatch, no_cover, pytestconfig, record_property,
                          record_testsuite_property, record_xml_attribute,
                          recwarn, subtests, tmp_path, tmp_path_factory,
                          tmpdir, tmpdir_factory</span>
<span class="pytest-bad">>       use 'pytest --fixtures [testpath]' for help on them.</span>

test_confusing_error_message.py:1
<span class="pytest-ok">=========================== short test summary info ============================</span>
<span class="pytest-bad">ERROR</span> test_confusing_error_message.py::<span class="pytest-ok">test_refactored</span>
<span class="pytest-bad">=============================== </span><font color="#EF2929"><span class="pytest-ok">1 error</span></font><span class="pytest-bad"> in 0.39s ===============================</span>
</tt></pre>

--

# Fixture discovery

```python
def test_something(tmp_path: pathlib.Path) -> None:
    tmp_path.write_text(my_module.generate_text())
    assert "SOME_STRING" in my_module.read_path(tmp_path)
```

<style>

div.pytest-figure-container {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-evenly;
}

div.pytest-figure-container figure {
    max-width: 40dvw;
}

div.pytest-figure-container img {
    max-width: 45dvw;
    max-height: 45dvh;
    height: auto;
}

div.pytest-figure-container figure figcaption {
    font-size: 0.7em;
    font-style: italic;
}
</style>

<div class="pytest-figure-container">
<figure class="fragment disappearing-fragment nospace-fragment fade-out" data-fragment-index="0">
<img src="external-images/fixture_availability.svg"
     alt="A diagram showing the scope that fixtures are available in">
<figcaption>

Scope of fixture availability for fixtures defined in `conftest.py` files at different levels in the directory structure.
</figcaption>
</figure>

<figure class="fragment disappearing-fragment nospace-fragment fade-out" data-fragment-index="0">
<img src="external-images/fixture_availability_plugins.svg"
     alt="A diagram showing the scope that fixtures are available in with plugins"
     style="height: auto; max-width: 40dvw">
<figcaption>

Fixture availability with plugins installed
</figcaption>
</figure>

<img src="external-images/memes/pepe_silvia_upscaled.png"
     style="height: 50dvh; width: auto; max-height: 60dvh;"
     alt="Pepe Silvia meme: Charlie from It's Always Sunny in Philadelphia stands in front of a corkboard covered in deranged writing; he has a crazed look in his eye"
     class="fragment fade-in nospace-fragment" data-fragment-index="0"
     >

</div>

--

# Proposed improvements

```python
# Explicitly import your fixtures
from pytest.fixtures import tmp_path
from my_plugin import setup_globals

# Explicitly apply fixtures you want
@pytest.apply(tmp_path)
def test_something(tmp_path: pathlib.Path) -> None:
    tmp_path.write_text(my_module.generate_text())
    assert "SOME_STRING" in my_module.read_path(tmp_path)

# Example of a "function-scoped" autouse fixture
@pytest.use(setup_globals)
def test_something_with_globals():
    assert my_module.INITIALIZED_GLOBAL == "initialized"
```

<div class="code-separator"></div>

```python
@pytest.fixture
def random_user(username_base: str | None = None) -> str:
    user = User(username_base)
    user.create_user()
    yield user.username
    user.delete_user()

# Bind as part of the wrapper decorator
@pytest.apply(random_user, username_base="josé")
def test_usernames_with_accents(random_user: str) -> None:
    assert get_user(random_user).base == "josé"

# Allow parameterization directly in apply
@pytest.apply(random_user, [
    {"username_base": "josé"},
    ("minecraft_dude",),
    pytest.param(username_base="calvin"),
])
def test_username_base(random_user: str) -> None:
    assert get_user(random_user).base is not None
```
<!-- .element class="fragment fade-in" -->

<span class="footnote">

A reform along these lines was also [proposed by Abid Mujtaba](https://github.com/abid-mujtaba/testing-fixtures) in 2023
</span>

