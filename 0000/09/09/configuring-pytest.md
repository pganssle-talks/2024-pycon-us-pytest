# Configuring `pytest`

<img src="external-images/logos/pytest_logo.svg"
     class="splash"
     alt="The pytest logo"
     style="max-height: 30dvh"/>

- Command line flags
- Config files
- `conftest.py`

--

<!-- .slide: data-visibility="hidden" -->

# Command line flags: Test selection

`-k <expr>`: Specify which tests will run

<pre class="code-wrapper fragment disappearing-fragment nospace-fragment fade-out" data-fragment-index="0"><tt class="hljs">pytest -k test_rrule
<span class="pytest-ok">============================= test session starts ==============================</span>
collected 2096 items / <b><u>1534 deselected</u></b> / <b><u>562 selected</u></b>

tests/test_rrule.py <span class="pytest-pass">.................................................... [  9%]</span>
<span class="pytest-pass">........................................................................ [ 22%]</span>
<span class="pytest-pass">........................................................................ [ 34%]</span>
<span class="pytest-pass">........................................................................ [ 47%]</span>
<span class="pytest-pass">........................................................................ [ 60%]</span>
<span class="pytest-pass">........................................................................ [ 73%]</span>
<span class="pytest-pass">........................................................................ [ 86%]</span>
<span class="pytest-pass">........................................................</span><span class="pytest-warn">x</span><span class="pytest-pass">............... [ 98%]</span>
<span class="pytest-pass">......                                                                   [100%]</span>

<span class="pytest-pass">=============== </span><span class="pytest-good">561 passed</span>, <span class="pytest-warn">1534 deselected</span>, <span class="pytest-warn">1 xfailed</span><span class="pytest-pass"> in 1.99s ================</span>
</tt>
</pre>

<pre class="code-wrapper fragment disappearing-fragment fade-in-and-out" data-fragment-index="0"><tt class="hljs">$ pytest -v -k 'test_rrule and testSetCache'
<span class="pytest-ok">============================= test session starts ==============================</span>
<span class="pytest-ok">collected 2096 items / 2093 deselected / 3 selected                            </span>

tests/test_rrule.py::RRuleSetTest::testSetCachePost <span class="pytest-good">PASSED               [ 33%]</span>
tests/test_rrule.py::RRuleSetTest::testSetCachePostInternal <span class="pytest-good">PASSED       [ 66%]</span>
tests/test_rrule.py::RRuleSetTest::testSetCachePre <span class="pytest-good">PASSED                [100%]</span>

<span class="pytest-good">====================== </span><span class="pytest-pass">3 passed</span>, <span class="pytest-warn">2093 deselected</span><span class="pytest-good"> in 0.77s ======================</span></tt></pre>

--

<!-- .slide: data-visibility: hidden -->

# Command line flags: Test selection

`-m <expr>`: Select by markers

<pre class="code-wrapper"><tt class="hljs">$ pytest -m 'hypothesis'
<span class="pytest-ok">============================= test session starts ==============================</span>
<span class="pytest-ok">collected 2096 items / 2091 deselected / 5 selected                            </span>

tests/property/test_isoparse_prop.py <span class="pytest-good">.                                   [ 20%]</span>
tests/property/test_parser_prop.py <span class="pytest-good">..                                    [ 60%]</span>
tests/property/test_tz_prop.py <span class="pytest-good">..                                        [100%]</span>

<span class="pytest-good">====================== </span><span class="pytest-pass">5 passed</span>, <span class="pytest-warn">2091 deselected</span><span class="pytest-good"> in 1.61s ======================</span></tt></pre>
<br/>
<pre class="code-wrapper"><tt class="hljs">$ pytest -m 'not hypothesis'
<span class="pytest-ok">============================= test session starts ==============================</span>
<span class="pytest-ok">collected 2096 items / 5 deselected / 2091 selected                            </span>

docs/exercises/solutions/mlk_day_rrule_solution.py <span class="pytest-good">.                     [  0%]</span>
tests/test_easter.py <span class="pytest-good">................................................... [  2%]</span>
<span class="pytest-good">........................................................................ [  5%]</span>
tests/test_import_star.py <span class="pytest-good">.                                              [  7%]</span>
tests/test_imports.py <span class="pytest-good">........................</span><span class="pytest-warn">sss</span><span class="pytest-good">...                     [  9%]</span>
tests/test_internals.py <span class="pytest-good">....                                             [  9%]</span>
tests/test_isoparser.py <span class="pytest-good">................................................ [ 11%]</span>
<span class="pytest-good">........................................................................ [ 15%]</span>
<span class="pytest-good">........................................................................ [ 18%]</span>
                                                 ...
tests/test_utils.py <span class="pytest-good">.......                                              [100%]</span>

<span class="pytest-good">========== </span><span class="pytest-pass">2027 passed</span>, <span class="pytest-warn">47 skipped</span>, <span class="pytest-warn">5 deselected</span>, <span class="pytest-warn">17 xfailed</span><span class="pytest-good"> in 6.81s ==========</span></tt></pre>

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

--

<!-- .slide: data-visibility="hidden" -->

# Command line flags: Display

<pre class="code-wrapper"><tt class="hljs">$ pip install pygments
...

$ pytest -x --code-highlight=yes  # This flag is optional
<span class="pytest-ok">============================= test session starts ==============================</span>
<span class="pytest-ok">collected 29 items / 1 skipped                                                 </span>

test_bad_assert.py <span class="pytest-bad">F</span>

=================================== FAILURES ===================================
<font color="#EF2929"><span class="pytest-ok">_______________________________ test_bad_assert ________________________________</span></font>

    <font color="#729FCF">def</font> <font color="#4BE234">test_bad_assert</font>():
        a = <font color="#729FCF">1</font>
>       <font color="#729FCF">assert</font> a == <font color="#729FCF">2</font>, <span class="pytest-warn">"Custom error message"</span>
<font color="#EF2929"><span class="pytest-ok">E       AssertionError: Custom error message</span></font>
<font color="#EF2929"><span class="pytest-ok">E       assert 1 == 2</span></font>

<font color="#EF2929"><span class="pytest-ok">test_bad_assert.py</span></font>:3: AssertionError
<span class="pytest-ok">=========================== short test summary info ============================</span>
<span class="pytest-bad">FAILED</span> test_bad_assert.py::<span class="pytest-ok">test_bad_assert</span> - AssertionError: Custom error message
<span class="pytest-bad">!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!!!!!</span>
<span class="pytest-bad">=================== </span><font color="#EF2929"><span class="pytest-ok">1 failed</span></font>, <span class="pytest-warn">1 skipped</span>, <span class="pytest-warn">1 warning</span><span class="pytest-bad"> in 0.28s ====================</span>
</tt></pre>

--

# Command line flags: Display

<!-- .slide: data-visibility: hidden -->

- `-l` / `--showlocals`: Show local variables in tracebacks


<pre class="code-wrapper"><tt class="hljs">$ pytest -k 'test_timestamp' -l
<span class="pytest-ok">============================= test session starts ==============================</span>
<span class="pytest-ok">collected 29 items / 28 deselected / 1 skipped / 1 selected                    </span>

test_error_message.py <span class="pytest-bad">F                                                  [100%]</span>

=================================== FAILURES ===================================
<font color="#EF2929"><span class="pytest-ok">________________________________ test_timestamp ________________________________</span></font>

    def test_timestamp():
        for dt_1, dt_2 in get_datetimes():
            ts2 = dt_2.timestamp()
            dt_rt = dt_1 + (dt_2 - dt_1)
>           assert ts2 == dt_rt.timestamp()
<font color="#EF2929"><span class="pytest-ok">E           AssertionError: assert 1715822040.0 == 1715818440.0</span></font>
<font color="#EF2929"><span class="pytest-ok">E            +  where 1715818440.0 = <built-in method timestamp of datetime.datetime object at 0x7885c6cbb2d0>()</span></font>
<font color="#EF2929"><span class="pytest-ok">E            +    where <built-in method timestamp of datetime.datetime object at 0x7885c6cbb2d0> = datetime.datetime(2024, 5, 15, 20, 14,
                               tzinfo=zoneinfo.ZoneInfo(key='America/New_York')).timestamp</span></font>

dt_1       = datetime.datetime(1970, 1, 1, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='America/New_York'))
dt_2       = datetime.datetime(2024, 5, 16, 1, 14, tzinfo=zoneinfo.ZoneInfo(key='UTC'))
dt_rt      = datetime.datetime(2024, 5, 15, 20, 14, tzinfo=zoneinfo.ZoneInfo(key='America/New_York'))
ts2        = 1715822040.0

<font color="#EF2929"><span class="pytest-ok">test_error_message.py</span></font>:33: AssertionError
<span class="pytest-bad">============ </span><font color="#EF2929"><span class="pytest-ok">1 failed</span></font>, <span class="pytest-warn">1 skipped</span>, <span class="pytest-warn">28 deselected</span>, <span class="pytest-warn">1 warning</span><span class="pytest-bad"> in 0.18s ============</span>
</tt></pre>

--

# Configuration files:


<div class="side-by-side">
<div class="left" style="width:40dvw">

<b><tt>pytest.ini</tt></b>

```ini
[pytest]
xfail_strict=True
minversion = 6.0
addopts = -ra -q
testpaths =
    tests
    integration
```
</div>
<div class="right" style="width:40dvw">

<b><tt>pyproject.toml</tt></b>

```toml
[tool.pytest.ini_options]
minversion = "6.0"
xfail_strict=true
addopts = "-ra -q"
testpaths = [
    "tests",
    "integration",
]
```
</div>
</div>

<br/>

<span style="font-size: 0.8em">

- Can also go in `[pytest]` section of `tox.ini` or `[tool:pytest]` section of `setup.cfg`, but `pyproject.toml` or `pytest.ini` are preferred.

</span>

--

## Set `xfail` to strict-by-default

```toml
[tool.pytest.ini_options]
xfail_strict=true
```

<br/><br/>

## Treat errors as warnings

```toml
[tool.pytest.ini_options]
filterwarnings = [
    "error",
    "error::DeprecationWarning",
    "error:PendingDeprecationWarning",
    "ignore::ErroneousWarning:erroneousmodule",
]
```

<br/><br/>

## Specify test patterns

```toml
[tool.pytest.ini_options]
python_files = [
    "test_*.py",
    "*_example.py",
]
```

--

# `conftest.py`

- Can put fixtures in this to be shared across multiple directories
- One can exist in any test directory, each scoped to all directories below it in the hierarchy
- Location for all hooks for plugins (to modify test execution and collection)

<br/><br/>


```python
# Configure pytest to ignore xfailing tests
def pytest_collection_modifyitems(items):
    for item in items:
        marker_getter = getattr(item, 'get_closest_marker', None)
        marker = marker_getter('xfail')

        # Need to query the args because conditional xfail tests still have
        # the xfail mark even if they are not expected to fail
        if marker and (not marker.args or marker.args[0]):
            item.add_marker(pytest.mark.no_cover)
```
