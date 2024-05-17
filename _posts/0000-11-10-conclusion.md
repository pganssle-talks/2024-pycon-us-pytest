# Recap

<div class="centered-container">

<div class="left-container" style="width: 100%">

### `pytest` can be adopted incrementally

- Use it just as a test runner
- Can mix-and match `pytest` and `unittest` style code

</div>

<div></div>

<div class="left-container" style="width: 100%">

### `pytest` is the standard way to do testing

- Broad ecosystem
- Strong documentation
- Under active development

</div>

<div></div>

<div class="left-container" style="width: 100%">

### `pytest` is extremely feature rich

- Fixtures
- Parameterization
- Much more! (`markers`, custom plugins, etc)

</div>
</div>

--

<div class="splash">
Thank you!
</div>

--

# Fixture UI Issues

<div class="centered-container big-code">

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

</div>

--

# Fixture discovery

<div class="big-code">

```python
def test_something(tmp_path: pathlib.Path) -> None:
    tmp_path.write_text(my_module.generate_text())
    assert "SOME_STRING" in my_module.read_path(tmp_path)
```
</div>

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

<div class="centered-container big-code">

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
<!-- .element class="fragment nospace-fragment disappearing-fragment fade-out" data-fragment-index="0" -->


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
<!-- .element class="fragment fade-in nospace-fragment" data-fragment-index="0" -->

<span class="footnote">

A reform along these lines was also [proposed by Abid Mujtaba](https://github.com/abid-mujtaba/testing-fixtures) in 2023
</span>

