# Major differences from `unittest`: `assert` statements

<div>

```python
def test_bad_assert(self):
    a = 1
    self.assertEqual(a, 2, "Custom error message")
```

<div class="code-separator"></div>

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

<div style="margin-bottom: 1em">

```python
def test_bad_assert(self):
    a = 1
    assert a == 2, "Custom error message"
```

<div class="code-separator"></div>

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

Notes:

So now that we've gotten that out of the way, let's take a look at some of the specific ways that pytest is magical. The first major difference you'll notice from `unittest` is that `pytest` uses the `assert` statement instead of these `assert` methods on the `TestCase` object. One reason that `unittest` and its derivatives use assert methods like `assertEqual` is that the `assert` statement just raises an assertion error on failure, and doesn't really give you any information about what caused the error.

With `assertEqual`, you are passing it both operands and telling it what notion of equality to use, and so the method is able to craft you a nice error message like "`a` doesn't equal `2`". If you were using bog standard `assert` statements, your testing framework would basically just be passed "a statement was true" or "a statement was false", plus any manually-written custom message you would want — meaning you'd basically need to manually and repetitively craft a bunch of error messages for every test.

--

# Major differences from `unittest`: `assert` statements

```python
def test_bad_assert():
    a = 1
    assert a == 2, "Custom error message"
```

<div class="code-separator"></div>

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

Notes:

This is the first way that `pytest` is magical — because with `pytest`, even though you are using `assert` statements, it still gives you a nice clean error message, including the operands and the operation that happened. The way it does this is that before it executes any test code, it actually compiles your tests into bytecode, then re-writes the bytecode to extract the relevant information and change what error messages are being raised.

Another reason that `unittest` avoids the `assert` statement is that `python` ignores all `assert` statements when it's run with `-O`, so if these `assert` statements aren't being executed in your test code, it's not possible to test that your code works when run with `-O`! Again, `pytest`'s byte code re-writing saves us here, because `pytest` specifically rewrites the byte code for `assert` statements *in test code* to no longer actually use the `assert` statement under the hood, leaving the `assert` statements in your module alone, so you can still run your tests in the optimized configuration.

--

```python
def test_bad_assert():
    a = 1
    assert (
        a == 2,
        "My very long error message doesn't fit on one line, gotta break it up"
    )
```

<div class="code-separator"></div>

```python
def test_bad_assert():
    a = 1
    assert a == 2, \
        "My very long error message doesn't fit on one line, gotta break it up"

```
<!-- .element class="fragment disappearing-fragment nospace-fragment fade-out" data-fragment-index="0" -->

```python
def test_bad_assert():
    a = 1
    assert tuple(
        a ==2,
        "My very long error message doesn't fit on one line, gotta break it up"
    )
```
<!-- .element class="fragment nospace-fragment fade-in" data-fragment-index="0" -->

<div class="code-separator"></div>

<pre class="code-wrapper fragment fade-in" data-fragment-index="1">
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

Notes:

The last problem with `assert` statements — and this is a problem with `assert` in general, not just in testing, is that it is subject to this particularly nasty and easy-to-overlook bug. Looking at these two code blocks, you expect them to be equivalent, right? The first one is just the second one but instead of a line continuation you've wrapped the arguments to `assert` in parentheses.

But in reality, what's happened is that the first block is equivalent to *this* block — you've taken the *two* arguments passed to the `assert` statement, and turned them into *one* argument — a non-empty `tuple`, which always evaluates to `True`, and thus this `assert` statement is a no-op. `pytest` doesn't fix this problem out of the box, necessarily, but it *does* raise a warning, and it is easy to configure `pytest` to elevate that to an exception. In practice, I've never actually seen this error personally, but I do know that it is fairly common.

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

Notes:

Now we've seen some problems that can be used by using bare `assert` methods, but we haven't seen the advantages that would lead `pytest` to go out of their way to implement byte code rewriting just to use this style. So why do this at all?

Well, one of the big advantages is that you don't need a huge proliferation of custom `assert` methods for every little operation you might want to do. Since `pytest` is able to extract out the relevant operations, you can just use natural comparisons with their normal semantics.

It even does this nifty thing where if one of the operands is a function call, it shows you both the result that didn't compare equal *and* the function call that produced the result. In `absltest` there's a one-off extension for the common case where that function is `len`, but this approach is much more scalable, since it doesn't require custom assert methods for any function you might want to call.

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

<div class="code-separator"></div>

<pre class="code-wrapper">
<tt class="hljs"><span class="pytest-bad">________________________________ test_float_bad ________________________________</span>

    def test_float_bad():
        a = 0.1 + 0.2
<span class="pytest-error">>       assert a == 0.3
E       assert 0.30000000000000004 == 0.3

test_floats.py</span>:5: AssertionError
</tt>
</pre>

Notes:

That's all well and good, you may say, but what about floats? Don't we *need* custom assertion functions for when we want fuzzy matches? Or are we supposed to write our own custom equality function just for fuzzy float comparisons?

For that case, you can use `pytest`'s built-in wrapper function, `approx`, which takes float objects and wraps them in an object whose equality semantics are fuzzy. You can also extend this in general — rather than defining a custom assertion method, you can define custom comparison semantics, and use the normal assertion methods.
