# Major differences from `unittest`: `assert` statements

<div style="margin-bottom: 1em">

```python
def test_bad_assert(self):
    a = 1
    assert a == 2, "Custom error message"
```

<br/>

```txt
$ python -m unittest
F
======================================================================
FAIL: test_bad_assert (test_bad_assert.Tests.test_bad_assert)
----------------------------------------------------------------------
Traceback (most recent call last):
  File ".../test_bad_assert.py", line 7, in test_bad_assert
    assert a == 2
AssertionError: Custom error message
----------------------------------------------------------------------
```
</div>

<div class="fragment fade-in">

```python
def test_bad_assert(self):
    a = 1
    self.assertEqual(a, 2, "Custom error message")
```

<br/>

```txt
$ python -m unittest
F
======================================================================
FAIL: test_bad_assert (test_bad_assert.Tests.test_bad_assert)
----------------------------------------------------------------------
Traceback (most recent call last):
  File ".../test_bad_assert.py", line 10, in test_bad_assert
    self.assertEqual(a, 2, "Custom error message")
AssertionError: 1 != 2 : Custom error message

----------------------------------------------------------------------
```

</div>

--

# Major differences from `unittest`: `assert` statements

```python
def test_bad_assert():
    a = 1
    assert a == 2, "Custom error message"
```

<div style="margin-top: 0.5em; margin-bottom: 0.5em">

<pre class="code-wrapper">
<tt class="hljs">$ pytest
test_bad_assert.py <span class="pytest-bad">F                                                   [100%]</span>

================================== FAILURES ==================================
<span class="pytest-bad">______________________________ <b>test_bad_assert</b> _______________________________</span>

    def test_bad_assert():
        a = 1
>       assert a == 2, "Custom error message"
<span class="pytest-error">E       AssertionError: Custom error message</span>
<span class="pytest-error">E       assert 1 == 2</span>

<span class="pytest-error">test_bad_assert.py</span>:3: AssertionError
========================== short test summary info ===========================
FAILED test_bad_assert.py::test_bad_assert - AssertionError: Custom error message
<span class="pytest-bad">============================= <b>1 failed</b> in 0.10s ==============================</span>

</tt>
</pre>
</div>

- Achieved by re-writing the bytecode before execution
- Works with assertions disabled (`python -O`)

--

```python
def test_bad_assert():
    a = 1
    assert (
        a == 2,
        "My very long error message doesn't fit on one line, gotta break it up"
    )
```
<br/>


<pre class="code-wrapper fragment fade-in">
<tt class="hljs">$ pytest test_bad_assert.py 
<span class="pytest-ok">============================= test session starts ==============================</span>
test_bad_assert.py <span class="pytest-pass">.</span>                                                     <span class="pytest-warn">[100%]</span>

<span class="pytest-warn">=============================== warnings summary ===============================</span>
test_bad_assert.py:7
  .../test_bad_assert.py:7: PytestAssertRewriteWarning: assertion is always
                            true, perhaps remove parentheses?
    assert (

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
<span class="pytest-warn">========================= <span class="pytest-pass">1 passed</span>, <span class="pytest-warning-count">1 warning</span> in 1.13s =========================
</tt>
</pre>

---

# Advantage: No need for custom `assert` methods

```python
def test_special_asserts():
    a = (1, 2, 3)
    assert a is not None       # self.assertIsNot(a, None)
    assert a < (2, 3, 4)       # self.assertLess(a, (2, 3, 4))
    assert len(a) == 4         # self.assertLen(a, 4) - absltest extension
```

<br/>

<pre class="code-wrapper">
<tt class="hljs"><span class="pytest-bad">_____________________________ test_special_asserts _____________________________</span>

    def test_special_asserts():
        a = (1, 2, 3)
        assert a is not None       # self.assertIsNot(a, None)
        assert a < (2, 3, 4)       # self.assertLess(a, (2, 3, 4))
<span class="pytest-error">>       assert len(a) == 4         # self.assertLen(a, 4) - absltest extension
E       assert 3 == 4
E        +  where 3 = len((1, 2, 3))

test_special_assert.py</span>:5: AssertionError
</tt>
</pre>

--

# Handling floats

```python
import pytest

def test_float_bad():
    a = 0.1 + 0.2
    assert a == 0.3


def test_float_good():
    a = 0.1 + 0.2
    assert a == pytest.approx(0.3)
```

<br/>

<pre class="code-wrapper">
<tt class="hljs"><span class="pytest-bad">________________________________ test_float_bad ________________________________</span>

    def test_float_bad():
        a = 0.1 + 0.2
<span class="pytest-error">>       assert a == 0.3
E       assert 0.30000000000000004 == 0.3

test_floats.py</span>:5: AssertionError
</tt>
</pre>








