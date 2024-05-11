# `pytest` is compatible with `unittest`

<div class="side-by-side">

<div class="left">

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

</div>
<div class="right">
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

--

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

<pre class="code-wrapper fragment nospace-fragment fade-in" data-fragment-index="0"><tt class="hljs">$ pytest test_error_message.py <b>--showlocals</b>
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

--

<img id="splash" class="splash"
     src="images/screenshots/junitxml_output.jpg"
     alt="Screenshot of the pytest documentation showing how to create output files in the JUnitXML format"
     >

<span class="footnote">

`pytest` has many options related to configuring test output, see [the documentation here](https://docs.pytest.org/en/7.1.x/how-to/output.html)
</span>
