# Error Messages: `unittest`

```python
class Tests(unittest.TestCase):
    def test_timestamp(self):
        for dt_1, dt_2 in get_datetimes():
            ts2 = dt_2.timestamp()
            dt_rt = dt_1 + (dt_2 - dt_1)
            self.assertEqual(ts2, dt_rt.timestamp())
```

<div class="code-separator"></div>

<div class="side-by-side">

<div class="left">

### `unittest`

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
<div class="right fragment fade-in nospace-fragment" data-fragment-index="0">

### `pytest`

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

Another nice advantage of `pytest` is the way it displays errors when a test fails. Take for example this test, which generates a bunch of datetimes and tests to see if they satisfy this property. You'll notice that with `unittest`, the result you get is not exactly useful, since the operands to `assertEqual` are both just large numbers, with no indication of what datetimes were involved. Writing an equivalent test with `pytest` gives this error message, which gives a lot more information about what went wrong.

You may also think I'm putting my thumb on the scales by including all this bolding and red text and such, but that's another difference between `pytest` and `unittest` — `unittest` gives plain text output, whereas `pytest` makes use of color and bolding, and in fact if you have `pygments` installed, you can even get it to show you syntax highligting.

--

# Command line flags: Debugging

- `-x`: Exit on first failure
- `--maxfail`: Exit after the first `num` failures or errors
- `--sw`/`--stepwise`: Exit on test failure, then continue from last failing test

<br/><br/>

- `--nf` / `--new-first`: Run tests ordered by last modified time of the file
- `--ff` / `--failed-first`: Start with tests that failed last time
- `--lf` / `--last-failed`: Only run tests that failed last time

<br/><br/>

- `--pdb`: Drop into debugger on failure
