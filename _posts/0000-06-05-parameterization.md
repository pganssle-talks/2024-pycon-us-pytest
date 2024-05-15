# Test paramet<span style="color:#D2D2D2">e</span>rization

<div class="centered-container big-code">
<div class="left-container">

```python
@pytest.mark.parametrize("dt_str", [
    "2025-01-01T01+00:00",
    "2025-01-01T01:00+00:00",
    "2025-01-01T01:00:00+00:00",
    pytest.param("2025-01-01T01:00:00Z",
                 marks=pytest.mark.xfail(sys.version_info < (3, 11),
                                         reason="Z is not supported")),
])
def test_fromisoformat(dt_str: str) -> None:
    expected_datetime = datetime(2025, 1, 1, 1, tzinfo=UTC)
    assert datetime.fromisoformat(dt_str) == expected_datetime
```

<br/>

<pre class="code-wrapper">
<tt class="hljs">$ pytest -v
<span class="pytest-ok">============================= test session starts ==============================</span>
<span class="pytest-ok">collected 4 items                                                              </span>

...::test_fromisoformat[2025-01-01T01+00:00] <span class="pytest-good">PASSED [ 25%]</span>
...::test_fromisoformat[2025-01-01T01:00+00:00] <span class="pytest-good">PASSED [ 50%]</span>
...::test_fromisoformat[2025-01-01T01:00:00+00:00] <span class="pytest-good">PASSED [ 75%]</span>
...::test_fromisoformat[2025-01-01T01:00:00Z] <span class="pytest-warn">XFAIL</span><span class="pytest-good"> [100%]</span>

<span class="pytest-ok">=========================== short test summary info ============================</span>
<span class="pytest-warn">XFAIL</span> ...::test_fromisoformat[2025-01-01T01:00:00Z] - Z is not supported
<span class="pytest-good">========================= <span class="pytest-pass">3 passed</span>, <span class="pytest-bad">1 xfailed</span> in 0.10s =========================</span>
</tt>
</pre>

</div>
</div>

--

# `unittest_parametrize`

<div class="centered-container big-code">

```python
import unittest_parametrize
from unittest_parametrize import parametrize, param

class Tests(unittest_parametrize.ParametrizedTestCase):
    @parametrize("dt_str", [
        ("2025-01-01T01+00:00",),
        ("2025-01-01T01:00+00:00",),
        ("2025-01-01T01:00:00+00:00",),
    ])
    def test_fromisoformat(self, dt_str):
        expected_datetime = datetime(2025, 1, 1, 1, tzinfo=UTC)
        self.assertEqual(datetime.fromisoformat(dt_str), expected_datetime)

```

<div></div>


```txt
$ python -m unittest -v parameterize
test_fromisoformat_0 (parameterize.Tests.test_fromisoformat_0) ... ok
test_fromisoformat_1 (parameterize.Tests.test_fromisoformat_1) ... ok
test_fromisoformat_2 (parameterize.Tests.test_fromisoformat_2) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

<div></div>
<div></div>
<div></div>

--

<!-- .slide: data-visibility="hidden" -->

# `unittest_parametrize`


<table class="alignment-table">
<tr>
<td>

```python
    @parametrize("x,expected", [
        param(1, 1),
        param(2, 4),
        param(0, 0, id="zero"),
        param(-4, 16, id="negative"),
    ])
    def test_square(self, x, expected):
        self.assertEqual(x**2, expected)
```
<!-- .element class="fragment disappearing-fragment fade-out" data-fragment-index="0" -->

```python
    @parametrize("x,expected", [
        (1, 1),
        (2, 4),
        (0, 0),
        (-4, 16),
    ], ids=[None, None, "zero", "negative"])
    def test_square(self, x, expected):
        self.assertEqual(x**2, expected)
```
<!-- .element class="fragment disappearing-fragment fade-in" data-fragment-index="0" -->

</td>

<td>

```python
@pytest.mark.parametrize("x,expected", [
    pytest.param(1, 1),
    pytest.param(2, 4),
    pytest.param(0, 0, id="zero"),
    pytest.param(-4, 16, id="negative"),
])
def test_square(x, expected):
    assert x**2 == expected
```
<!-- .element class="fragment disappearing-fragment fade-out" data-fragment-index="0" -->

```python
@pytest.mark.parametrize("x,expected", [
    (1, 1),
    (2, 4),
    (0, 0),
    (-4, 16),
], ids=[None, None, "zero", "negative"])
def test_square(x, expected):
    assert x**2 == expected
```
<!-- .element class="fragment disappearing-fragment fade-in" data-fragment-index="0" -->

</td>
</tr>

<tr><td colspan="2"><div class="code-separator"></div></td></tr>

<tr>
<td>

```txt
test_square_0 (parameterize.Tests.test_square_0) ... ok
test_square_1 (parameterize.Tests.test_square_1) ... ok
test_square_negative (parameterize.Tests.test_square_negative) ... ok
test_square_zero (parameterize.Tests.test_square_zero) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s
```

</td>
<td>

<pre class="code-wrapper"><tt class="hljs">$ pytest -v
<span class="pytest-ok">============================= test session starts ==============================</span>
<span class="pytest-ok">collected 4 items                                                              </span>

...::test_square[1-1] <span class="pytest-pass">PASSED                         [ 25%]</span>
...::test_square[2-4] <span class="pytest-pass">PASSED                         [ 50%]</span>
...::test_square[zero] <span class="pytest-pass">PASSED                        [ 75%]</span>
...::test_square[negative] <span class="pytest-pass">PASSED                    [100%]</span>

<span class="pytest-pass">============================== </span><span class="pytest-good">4 passed</span><span class="pytest-pass"> in 0.14s ===============================</span>
</tt></pre>

</td>
</tr>
</table>


--

# Stacking parametrize decorators

<div class="centered-container medium-code">

<div class="left-container" style="width:100%">

```python
@pytest.mark.parametrize("x", [4, 5, 6])
@pytest.mark.parametrize("y", [3, 2, 1])
def test_multiply(x, y):
    z = x * y
    assert z > x and z > y
```

<div></div>

<pre class="code-wrapper"><tt class="hljs">$ pytest --tb=short
<span class="pytest-ok">============================= test session starts ==============================</span>
<span class="pytest-ok">collected <u>9</u> items                                                              </span>

<span class="pytest-pass">.........</span><span class="pytest-bad">FFF                                                              [100%]</span>

=================================== FAILURES ===================================
<span class="pytest-error">______________________________ test_multiply[1-4] ______________________________</span>
<span class="pytest-error">...</span>:7: in test_multiply
    assert z &gt; x and z &gt; y
<span class="pytest-error">E   assert (4 &gt; 4)</span>
<span class="pytest-error">______________________________ test_multiply[1-5] ______________________________</span>
<span class="pytest-error">...</span>:7: in test_multiply
    assert z &gt; x and z &gt; y
<span class="pytest-error">E   assert (5 &gt; 5)</span>
<span class="pytest-error">______________________________ test_multiply[1-6] ______________________________</span>
<span class="pytest-error">...</span>:7: in test_multiply
    assert z &gt; x and z &gt; y
<span class="pytest-error">E   assert (6 &gt; 6)</span>
<span class="pytest-ok">=========================== short test summary info ============================</span>
<span class="pytest-bad">FAILED</span> ...::<b>test_multiply[1-4]</b> - assert (4 &gt; 4)
<span class="pytest-bad">FAILED</span> ...::<b>test_multiply[1-5]</b> - assert (5 &gt; 5)
<span class="pytest-bad">FAILED</span> ...::<b>test_multiply[1-6]</b> - assert (6 &gt; 6)
<span class="pytest-bad">========================= </span><span class="pytest-error">3 failed</span>, <span class="pytest-pass">6 passed</span><span class="pytest-bad"> in 0.23s ==========================</span>
</tt>
</pre>

<img src="images/memes/doge-parameterization.png"
     alt="Doge meme featuring a Shiba Inu with text in Comic Sans reading, 'how can this b?', 'so text matrix', 'many wow', 'such cartesian product'"
     style="height: auto; width: 30dvw; position: fixed; top: 3.5em; right: 3dvw; border: 3px solid #000">

</div>
</div>

--

# Subtests

<div class="centered-container">
<div class="left-container" style="width: 100%">

```python
def test_fromisoformat(self):
    cases = [
        "2025-01-01T01+00:00",
        "2025-01-01T01:00+00:00",
        "badstring",                      # Raises exception
        "2025-01-01T01:00:00+00:00",
        "2025-01-01T02:00:00+00:00",      # Value is wrong
    ]
    expected_datetime = datetime(2025, 1, 1, 1, tzinfo=UTC)

    for case in cases:
        with self.subTest(case):
            self.assertEqual(datetime.fromisoformat(case), expected_datetime)
```

<div></div>

```txt
$ python -m unittest -vv test_subtests.py
test_fromisoformat (test_subtests.Tests.test_fromisoformat) ...
  test_fromisoformat (test_subtests.Tests.test_fromisoformat) [badstring] ... ERROR
  test_fromisoformat (test_subtests.Tests.test_fromisoformat) [2025-01-01T02:00:00+00:00] ... FAIL

======================================================================
ERROR: test_fromisoformat (test_subtests.Tests.test_fromisoformat) [badstring]
----------------------------------------------------------------------
Traceback (most recent call last):
    self.assertEqual(datetime.fromisoformat(case), expected_datetime)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: Invalid isoformat string: 'badstring'
======================================================================
FAIL: test_fromisoformat (test_subtests.Tests.test_fromisoformat) [2025-01-01T02:00:00+00:00]
----------------------------------------------------------------------
AssertionError: datetime.datetime(2025, 1, 1, 2, 0, tzinfo=datetime.timezone.utc) !=
                datetime.datetime(2025, 1, 1, 1, 0, tzinfo=datetime.timezone.utc)
----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1, errors=1)
```

</div>
</div>


--

# Subtests

<div class="centered-container" style="justify-content: flex-start">
<div class="left-container" style="width: 100%">

```python
def test_datetime(self):
    dt = datetime(2020, 3, 28, 12, tzinfo=ZoneInfo("Europe/London"))
    exp_tzname, exp_utcoffset = ("GMT", timedelta(0))
    with self.subTest("tzname"):
        self.assertEqual(dt.tzname() == expected_tzname)

    with self.subTest("offset"):
        self.assertEqual(dt.utcoffset(), expected_utcoffset)
```
<!-- .element class="fragment disappearing-fragment nospace-fragment fade-out" data-fragment-index="0" -->

```python
def test_datetime(subtests):            # Using the pytest-subtests plugin
    dt = datetime(2020, 3, 28, 12, tzinfo=ZoneInfo("Europe/London"))
    exp_tzname, exp_utcoffset = ("GMT", timedelta(0))
    with subtests.test(msg="tzname"):
        assert dt.tzname() == expected_tzname

    with subtests.test(msg="offset"):
        assert dt.utcoffset() == expected_utcoffset
```
<!-- .element class="fragment nospace-fragment fade-in" data-fragment-index="0" -->

<div></div>

```python
def datetime_test_cases():
    GMT = ("GMT", timedelta(0))
    BST = ("BST", timedelta(1))
    zi = ZoneInfo("Europe/London")

    return [
        (datetime(2020, 3, 28, 12, tzinfo=zi), GMT),
        (datetime(2020, 3, 29, 12, tzinfo=zi), BST),
        (datetime(2020, 10, 24, 12, tzinfo=zi), BST),
        (datetime(2020, 10, 25, 12, tzinfo=zi), GMT),
    ]

@pytest.mark.parameterize("dt, offset", datetime_test_cases())
def test_europe_london(subtests, dt, offset):
    exp_tzname, exp_utcoffset = offset
    with subtests.test(msg="tzname", dt=dt):
        assert dt.tzname() == exp_tzname

    with subtests.test(msg="utcoffset", dt=dt):
        assert dt.utcoffset() == exp_utcoffset
```
<!-- .element class="fragment fade-in" data-fragment-index="1" -->

</div>

<span class="footnote">For more on subtests, see my blog post [Subtests in Python](https://blog.ganssle.io/articles/2020/04/subtests-in-python.html)</span>

</div>
