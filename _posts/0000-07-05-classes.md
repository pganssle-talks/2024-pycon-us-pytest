# Classes are optional in `pytest`

<div class="centered-container big-code">

<div class="side-by-side" style="margin-bottom:1em">
<div class="left" style="width: 40dvw; font-size: 1.25em; text-align: left">

```python
class ExampleTest(unittest.TestCase):
    def test_basic(self):
        a = 4
        b = 4

        self.assertEqual(a, b)
```

</div>
<div class="right" style="width: 40dvw; font-size: 1.25em">

```python
def test_basic():
    a = 4
    b = 4
    assert a == b
```

</div>
</div>

- Test cases are discovered based on [naming conventions (configurable)](https://docs.pytest.org/en/7.1.x/example/pythoncollection.html).
    - Files: `test_*.py`, `*_test.py`
    - Tests: `test_*`
    - Classes: `Test*`
- Most setup/teardown use cases are handled with fixtures
- `pytest` also supports using classes

<div></div>

</div>

--

# Using classes in `pytest`

<div class="side-by-side">

<div class="left" style="width:55dvw; max-width:55dvw; font-size:1.3em">

```python
class TestClass:
    @classmethod
    def setup_class(cls):
        """Run when class is initialized."""
        cls.EXPENSIVE_GLOBAL = generate_expensive_global()


    @classmethod
    def teardown_class(cls):
        """Run when class is destroyed."""
        cls.EXPENSIVE_GLOBAL.free_resources()


    def setup_method(self, method):
        """Run before every test method execution."""


    def teardown_method(self, method):
        """Run after every test method execution."""


    def test_method(self):
        """This is a test that is actually run."""
        assert 1 == 1
```
</div>
<div class="right" style="width: 30dvw; font-size: 0.75em; align-self: flex-start">

- `{setup,teardown}_module(module)` also available
- `{setup,teardown}_function(func)` works with bare test functions

</div>

</div>

