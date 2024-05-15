# Markers

*Adds some metadata to a test*

```python
def test_light_thing():
    assert 1 + 1 == 2

@pytest.mark.heavy
def test_heavy_thing():
    assert calculate_digit_of_e(1_000_000_000) == 4
```

<br/>
<pre class="code-wrapper">
<tt class="hljs">$ pytest -k 'not heavy' pytest/test_marks.py
<span class="pytest-ok">============================= test session starts ==============================</span>
collected 2 items / 1 deselected / 1 selected
..//test_marks.py <span class="pytest-pass">.                                                   [100%]</span>
<span class="pytest-good">======================= <span class="pytest-pass">1 passed</span>, <span class="pytest-warn">1 deselected</span> in 0.15s ========================</span>
</tt>
</pre>

<br/>

```python
def test_build_exists():
    assert BUILD_PATH.exists()

@pytest.mark.depends(on="test_build_exists")
def test_build_succeeded():
    with open(BUILD_PATH / "pkg_info", "rt") as f:
        assert next(f) == "PKG_INFO_HEADER"
        ...
```
<!-- .element class="fragment fade-in" data-fragment-index="0" -->

<p class="footnote fragment fade-in" data-fragment-index="0">
Example using <a href="https://pypi.org/project/pytest-depends/"><tt>pytest-depends</tt></a>.
</p>

--

# `xfail` and `skip`

```python
@pytest.mark.skipif(sys.version_info < (3, 10), reason="Uses feature from 3.10")
def test_skipped():
    assert (14).bit_count() == 3


@pytest.mark.xfail(reason="Always fails")
def test_xfail():
    assert False

@pytest.mark.xfail(reason="Always fails")
def test_xpass():
    assert True
```

<br/>

<pre class="code-wrapper">
<tt class="hljs">$ pytest pytest/test_xfail.py
<span class="pytest-ok">============================= test session starts ==============================</span>

pytest/test_xfail.py <span class="pytest-warn">sx</span><span class="pytest-bad">F                                                 [100%]</span>

=================================== FAILURES ===================================
<span class="pytest-error">__________________________________ test_xpass __________________________________</span>
[XPASS(strict)] Always fails
<span class="pytest-ok">=========================== short test summary info ============================</span>
<span class="pytest-bad">FAILED</span> .../test_xfail.py::<b>test_xpass</b>
<span class="pytest-bad">=================== <span class="pytest-error">1 failed</span>, <span class="pytest-warn">1 skipped, 1 xfailed</span> in 0.04s ====================</span>
</tt>
</pre>

<span class="footnote">For more details see <a href="https://ganssle.io/talks/#xfail-and-skip"><i>my talk at PyTexas 2022</i></a> or <a href="https://blog.ganssle.io/articles/2021/11/pytest-xfail.html">one of my blog posts on the subject</a> (https://blog.ganssle.io) </span>
