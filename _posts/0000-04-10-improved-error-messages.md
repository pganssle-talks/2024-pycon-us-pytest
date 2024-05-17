# Improved error messages

<div class="left-container big-code">

```python
class Tests(unittest.TestCase):
    def test_timestamp(self):
        for dt_1, dt_2 in get_datetimes():
            ts2 = dt_2.timestamp()
            dt_rt = dt_1 + (dt_2 - dt_1)
            self.assertEqual(ts2, dt_rt.timestamp())
```
<!-- .element class="disappearing-fragment fragment nospace-fragment fade-out" data-fragment-index="0" -->

```python
class Tests(unittest.TestCase):
    def test_timestamp(self):
        for dt_1, dt_2 in get_datetimes():
            ts2 = dt_2.timestamp()
            dt_rt = dt_1 + (dt_2 - dt_1)
            assert ts2 == dt_rt.timestamp()
```
<!-- .element class="fragment nospace-fragment fade-in" data-fragment-index="0" -->

</div>

<div class="centered-container">

<div class="fragment disappearing-fragment nospace-fragment fade-out" data-fragment-index="0">

```txt
$ python -m unittest test_error_message.py 
F
======================================================================
FAIL: test_timestamp (test_error_message.Tests.test_timestamp)
----------------------------------------------------------------------
Traceback (most recent call last):
  File ".../test_error_message.py", line 35, in test_timestamp
    self.assertEqual(ts2, dt_rt.timestamp())
AssertionError: 1715822040.0 != 1715818440.0

----------------------------------------------------------------------
Ran 1 test in 0.003s

FAILED (failures=1)
```

</div>

<div class="fragment fade-in nospace-fragment" data-fragment-index="0">

<pre class="code-wrapper fragment disappearing-fragment nospace-fragment fade-out" data-fragment-index="1"><tt class="hljs"><span class="pytest-ok">============================= test session starts ==============================</span>
<span class="pytest-ok">collected 1 item                                                               </span>

test_error_message.py <span class="pytest-bad">F                                                  [100%]</span>

=================================== FAILURES ===================================
<span class="pytest-error">________________________________ test_timestamp ________________________________</span>

    def test_timestamp():
        for dt_1, dt_2 in get_datetimes():
            ts2 = dt_2.timestamp()
            dt_rt = dt_1 + (dt_2 - dt_1)
>           assert ts2 == dt_rt.timestamp()
<span class="pytest-error">E           AssertionError: assert 1715822040.0 == 1715818440.0</span>
<span class="pytest-error">E            +  where 1715818440.0 = &amp;lt;built-in method timestamp of datetime object ...&amp;gt;()</span>
<span class="pytest-error">E            +    where &amp;lt;built-in method timestamp of datetime object...&amp;gt; =
                datetime(2024, 5, 15, 20, 14,
                         tzinfo=ZoneInfo(key='America/New_York')).timestamp</span>

<span class="pytest-error">test_error_message.py</span>:33: AssertionError
<span class="pytest-ok">=========================== short test summary info ============================</span>
<span class="pytest-bad">FAILED</span> test_error_message.py::<span class="pytest-ok">test_timestamp</span> - AssertionError: assert 1715822040.0 == 1715818440.0
<span class="pytest-bad">============================== </span><span class="pytest-error">1 failed</span><span class="pytest-bad"> in 0.12s ===============================</span>
</tt></pre>

<pre class="code-wrapper fragment nospace-fragment fade-in" data-fragment-index="1"><tt class="hljs"><span class="pytest-ok">============================= test session starts ==============================</span>
<span class="pytest-ok">collected 1 item                                                               </span>

test_error_message.py <span class="pytest-bad">F                                                  [100%]</span>

=================================== FAILURES ===================================
<span class="pytest-error">________________________________ test_timestamp ________________________________</span>

    <font color="#729FCF">def</font> <font color="#4BE234">test_timestamp</font>():
        <font color="#729FCF">for</font> dt_1, dt_2 <font color="#AD7FA8">in</font> get_datetimes():
            ts2 = dt_2.timestamp()
            dt_rt = dt_1 + (dt_2 - dt_1)
>           <font color="#729FCF">assert</font> ts2 == dt_rt.timestamp()
<span class="pytest-error">E           AssertionError: assert 1715822040.0 == 1715818440.0</span>
<span class="pytest-error">E            +  where 1715818440.0 = &amp;lt;built-in method timestamp of datetime object...&amp;gt;()</span>
<span class="pytest-error">E            +    where &amp;lt;built-in method timestamp of datetime object...&amp;gt; =
                datetime(2024, 5, 15, 20, 14,
                         tzinfo=ZoneInfo(key='America/New_York')).timestamp</span>

<span class="pytest-error">test_error_message.py</span>:33: AssertionError
<span class="pytest-ok">=========================== short test summary info ============================</span>
<span class="pytest-bad">FAILED</span> test_error_message.py::<span class="pytest-ok">test_timestamp</span> - AssertionError: assert 1715822040.0 == 1715818440.0
<span class="pytest-bad">============================== </span><span class="pytest-error">1 failed</span><span class="pytest-bad"> in 0.20s ===============================</span>
</tt></pre>

</div>
</div>


Notes:

Another nice advantage of `pytest` is the way it displays errors when a test fails. For example take this test, which generates a bunch of datetimes and tests to see if they satisfy this property. You'll notice that with `unittest`, the result you get is not exactly useful, since the operands to `assertEqual` are both just large numbers, with no indication of what datetimes were involved.

Writing an equivalent test with `pytest` gives this error message, which gives a lot more information about what went wrong.

You may also think I'm putting my thumb on the scales by including all this bolding and red text and such, but that's another difference between `pytest` and `unittest` — `unittest` gives plain text output, whereas `pytest` makes use of color and bolding, and in fact if you have `pygments` installed, you can even get it to show you syntax highligting.

--

# `pytest` is compatible with `unittest`

<div class="centered-container">

<div class="left-container">

```txt
$ python -m unittest
F
======================================================================
FAIL: test_special_asserts (test_special_methods.Tests.test_special_asserts)
----------------------------------------------------------------------
Traceback (most recent call last):
  File ".../test_special_methods.py", line 8, in test_special_asserts
    self.assertEqual(len(a), 4)
AssertionError: 3 != 4

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

<div class="code-separator"></div>

<pre class="code-wrapper"><tt class="hljs">$ pytest test_special_methods.py
<span class="pytest-ok">============================= test session starts ==============================</span>
<span class="pytest-ok">collected 1 item                                                               </span>
test_special_methods.py <span class="pytest-bad">F                                                [100%]</span>
=================================== FAILURES ===================================
<span class="pytest-error">__________________________ Tests.test_special_asserts __________________________</span>
self = &amp;lt;test_special_methods.Tests testMethod=test_special_asserts&amp;gt;<br/>
<font color="#729FCF">def</font> <font color="#4BE234">test_special_asserts</font>(<font color="#34E2E2">self</font>):
    a = (<font color="#729FCF">1</font>, <font color="#729FCF">2</font>, <font color="#729FCF">3</font>)
    <font color="#34E2E2">self</font>.assertIsNot(a, <font color="#729FCF">None</font>)
    <font color="#34E2E2">self</font>.assertLess(a, (<font color="#729FCF">2</font>, <font color="#729FCF">3</font>, <font color="#729FCF">4</font>))
&amp;gt;       <font color="#34E2E2">self</font>.assertEqual(<font color="#34E2E2">len</font>(a), <font color="#729FCF">4</font>)
<span class="pytest-error">E       AssertionError: 3 != 4</span><br/>
<span class="pytest-error">test_special_methods.py</span>:8: AssertionError
<span class="pytest-ok">=========================== short test summary info ============================</span>
<span class="pytest-bad">FAILED</span> test_special_methods.py::<span class="pytest-ok">Tests::test_special_asserts</span> - AssertionError: 3 != 4
<span class="pytest-bad">============================== </span><span class="pytest-error">1 failed</span><span class="pytest-bad"> in 1.04s ===============================</span>
</tt></pre>

</div>
</div>

Notes:

In fact, you can get *some* of this advantage from `pytest` even without migrating your tests away from `unittest` style. You see, `pytest` is both a test runner and a testing framework, and the test runner is perfectly compatible with `unittest`. So you can basically get this nicely-formatted error message for free by switching to `pytest` as your test runner. That said, when you are using `unittest` test cases, you don't get the full benefit of the byte code rewriting, so you don't get that nice thing where `pytest` can tell you that when it says `3 != 4`, it means `len(a) != 4`.

--

<!-- <div style="position: absolute; top: 5%; left: 0; width: 100%" class="big-code"> -->
<div style="width: 100%" class="big-code">

<pre class="code-wrapper disappearing-fragment nospace-fragment fragment fade-out" data-fragment-index="0"><tt class="hljs">$ pytest test_error_message.py
<span class="pytest-ok">============================= test session starts ==============================</span>
<span class="pytest-ok">collected 1 item                                                               </span>

test_error_message.py <span class="pytest-bad">F                                                  [100%]</span>

=================================== FAILURES ===================================
<span class="pytest-error">_____________________________ Tests.test_timestamp _____________________________</span>

    <font color="#729FCF">def</font> <font color="#4BE234">test_timestamp</font>(<font color="#34E2E2">self</font>):
        <font color="#729FCF">for</font> dt_1, dt_2 <font color="#AD7FA8">in</font> get_datetimes():
            ts2 = dt_2.timestamp()
            dt_rt = dt_1 + (dt_2 - dt_1)
>           <font color="#34E2E2">self</font>.assertEqual(ts2, dt_rt.timestamp())
<span class="pytest-error">E           AssertionError: 1715822040.0 != 1715818440.0</span>

<span class="pytest-error">test_error_message.py</span>:35: AssertionError
<span class="pytest-ok">=========================== short test summary info ============================</span>
<span class="pytest-bad">FAILED</span> test_error_message.py::<span class="pytest-ok">Tests::test_timestamp</span> - AssertionError: 1715822040.0 != 1715818440.0
<span class="pytest-bad">============================== </span><span class="pytest-error">1 failed</span><span class="pytest-bad"> in 0.93s ===============================</span>
</tt></pre>

<pre class="code-wrapper fragment fade-in" data-fragment-index="0"><tt class="hljs">$ pytest test_error_message.py <b>--showlocals</b>
<span class="pytest-ok">============================= test session starts ==============================</span>
<span class="pytest-ok">collected 1 item                                                               </span>

test_error_message.py <span class="pytest-bad">F                                                  [100%]</span>

=================================== FAILURES ===================================
<span class="pytest-error">_____________________________ Tests.test_timestamp _____________________________</span>

    <font color="#729FCF">def</font> <font color="#4BE234">test_timestamp</font>(<font color="#34E2E2">self</font>):
        <font color="#729FCF">for</font> dt_1, dt_2 <font color="#AD7FA8">in</font> get_datetimes():
            ts2 = dt_2.timestamp()
            dt_rt = dt_1 + (dt_2 - dt_1)
&amp;gt;           <font color="#34E2E2">self</font>.assertEqual(ts2, dt_rt.timestamp())
<span class="pytest-error">E           AssertionError: 1715822040.0 != 1715818440.0</span>

dt_1       = datetime.datetime(1970, 1, 1, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='America/New_York'))
dt_2       = datetime.datetime(2024, 5, 16, 1, 14, tzinfo=datetime.timezone.utc)
dt_rt      = datetime.datetime(2024, 5, 15, 20, 14, tzinfo=zoneinfo.ZoneInfo(key='America/New_York'))
self       = &amp;lt;test_error_message.Tests testMethod=test_timestamp&amp;gt;
ts2        = 1715822040.0

<span class="pytest-error">test_error_message.py</span>:35: AssertionError
<span class="pytest-ok">=========================== short test summary info ============================</span>
<span class="pytest-bad">FAILED</span> test_error_message.py::<span class="pytest-ok">Tests::test_timestamp</span> - AssertionError: 1715822040.0 != 1715818440.0
<span class="pytest-bad">============================== </span><span class="pytest-error">1 failed</span><span class="pytest-bad"> in 0.92s ===============================</span>
</tt></pre>

</div>

Notes:

However, you actually can get *something* like that with the `pytest` test runner. Going back to our `datetime` example, you can see that when you are using a `TestCase`, `pytest` doesn't expand the operands like it does when you are using the bare assertion `pytest`-style tests, but if you pass `-l` or `--showlocals`, `pytest` will capture all the local variables that are in the scope of the test, and include them in the error message. It's a bit more verbose, but it gives a lot more information, and might even be something you want to use even if you are using `pytest` as your test framework as well.

--

# `pytest` as a test runner: flags

<div class="centered-container">

- `-x`: Exit on first failure
- `--maxfail`: Exit after the first `num` failures or errors
- `--sw`/`--stepwise`: Exit on test failure, then continue from last failing test

<div></div>

- `--nf` / `--new-first`: Run tests ordered by last modified time of the file
- `--ff` / `--failed-first`: Start with tests that failed last time
- `--lf` / `--last-failed`: Only run tests that failed last time

<div></div>

- `--pdb`: Drop into debugger on failure

<div></div>
</div>

--

<div class="centered-container">

<figure>
<img id="splash" class="splash"
     src="images/screenshots/junitxml_output.jpg"
     alt="Screenshot of the pytest documentation showing how to create output files in the JUnitXML format"
     >

<figcaption class="footnote">

`pytest` has many options related to configuring test output, see [the documentation here](https://docs.pytest.org/en/7.1.x/how-to/output.html)
</figcaption>
</figure>

</div>
