# Error Messages: `unittest`

```python
class Tests(unittest.TestCase):
    def test_timestamp(self):
        for dt_1, dt_2 in get_datetimes():
            ts2 = dt_2.timestamp()
            dt_rt = dt_1 + (dt_2 - dt_1)
            self.assertEqual(ts2, dt_rt.timestamp())
```

<br/>

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

<br/>

<pre class="code-wrapper fragment fade-in">
<tt class="hljs"><span class="pytest-bad">________________________________ test_timestamp ________________________________</span>

    def test_timestamp():
        for dt_1, dt_2 in get_datetimes():
            ts2 = dt_2.timestamp()
            dt_rt = dt_1 + (dt_2 - dt_1)
<span class="pytest-error">>           assert ts2 == dt_rt.timestamp()
E           AssertionError: assert 1715822040.0 == 1715818440.0
E            +  where 1715818440.0 = <built-in method timestamp of datetime.datetime object at 0x7154d82baf70>()
E            +    where <built-in method timestamp of datetime.datetime object at 0x7154d82baf70> = datetime.datetime(2024, 5, 15, 20, 14,
                                             tzinfo=zoneinfo.ZoneInfo(key='America/New_York')
                                             ).timestamp

test_error_message.py</span>:33: AssertionError
</tt>
</pre>

