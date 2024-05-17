# Plugins

<div class="centered-container">

<div class="left-container" style="width: 100%">

- `pytest-randomly`: Run tests in a random order
- `pytest-xdist`: Run tests in parallel
- `pytest-subtest`: Adds the `subtest` fixture
- `pytest-cov`: Orchestrates coverage with `pytest`

</div>

<div></div>

<div class="left-container" style="width: 100%">

- `pytest-memray`: Memory profiling
- `pytest-leaks`: Memory leak detection
- `pytest-benchmark` / `pytest-speed`: Speed benchmarks

</div>

<pre class="code-wrapper"><tt class="hljs">$ pytest --memray tests/test_easter.py
<span class="pytest-ok">============================= test session starts ==============================</span>
Using --randomly-seed=609276657
<span class="pytest-ok">collected 163 items                                                            </span>

tests/test_easter.py <span class="pytest-good">................................................... [ 31%]</span>
<span class="pytest-good">........................................................................ [ 75%]</span>
<span class="pytest-good">........................................                                 [100%]</span>


================================ MEMRAY REPORT =================================
Allocation results for tests/test_easter.py::test_easter_orthodox[easter_date9] at the high watermark

     📦 Total memory allocated: 1.4KiB
     📏 Total allocations: 2
     📊 Histogram of allocation sizes: |█ |
     🥇 Biggest allocating functions:
        - wrapper:pytest_memray/plugin.py:192 -> 844.0B
        - test_easter_orthodox:tests/test_easter.py:83 -> 614.0B
                       ...
</tt></pre>

</div>

--

# Plugins


<div class="centered-container">

<div class="left-container" style="width: 100%">

- `pygments`: Code highlighting  in tracebacks
- `pytest-hammertime`: Turns `.` into '🔨'
- `pytest-pumpkin-spice`: Adds "pumpkin spice" flavor to your output
- `pytest-sugar`: Changes look and feel of `pytest`

</div>

<pre class="code-wrapper fragment disappearing-fragment nospace-fragment fade-out" data-fragment-index="0"><tt class="hljs">$ pytest test_bad_assert.py
<span class="pytest-ok">============================= test session starts ==============================</span>
<span class="pytest-ok">collected 1 item                                                               </span>

test_bad_assert.py <span class="pytest-bad">F                                                     [100%]</span>

=================================== FAILURES ===================================
<span class="pytest-error">_______________________________ test_bad_assert ________________________________</span>

    <font color="#729FCF">def</font> <font color="#4BE234">test_bad_assert</font>():
        a = <font color="#729FCF">1</font>
>       <font color="#729FCF">assert</font> a == <font color="#729FCF">2</font>, <span class="pytest-warn">"Custom error message"</span>
<span class="pytest-error">E       AssertionError: Custom error message</span>
<span class="pytest-error">E       assert 1 == 2</span>

<span class="pytest-error">test_bad_assert.py</span>:3: AssertionError
<span class="pytest-ok">=========================== short test summary info ============================</span>
<span class="pytest-bad">FAILED</span> test_bad_assert.py::<span class="pytest-ok">test_bad_assert</span> - AssertionError: Custom error message
</tt></pre>

<pre class="code-wrapper fragment disappearing-fragment nospace-fragment fade-in-and-out" data-fragment-index="0"><tt class="hljs">$ pytest --pumpkin-spice pytest
<span class="pytest-ok">================================================ test session starts ================================================</span>
<span class="pytest-ok">collected 33 items / 1 skipped                                                                                      </span>

pytest/test_bad_assert.py <span class="pytest-bad">❄️                                                                                   [  3%]</span>
pytest/test_bad_asserts_tuple.py <span class="pytest-good">🎃 </span><span class="pytest-bad">                                                                           [  6%]</span>
pytest/test_classes.py <span class="pytest-bad">🥧                                                                                      [  9%]</span>
pytest/test_confusing_error_message.py <span class="pytest-bad">🥧                                                                      [ 12%]</span>
pytest/test_error_message.py <span class="pytest-bad">❄️                                                                                [ 15%]</span>
pytest/test_fixture_parameters.py <span class="pytest-good">🎃 🎃 🎃 </span><span class="pytest-bad">                                                                     [ 24%]</span>
pytest/test_floats.py <span class="pytest-bad">❄️ </span><span class="pytest-good">🎃 </span><span class="pytest-bad">                                                                                   [ 30%]</span>
pytest/test_marks.py <span class="pytest-good">🎃 </span><span class="pytest-bad">❄️                                                                                     [ 36%]</span>
pytest/test_parametrize_ids.py <span class="pytest-good">🎃 🎃 🎃 🎃 </span><span class="pytest-bad">                                                                     [ 60%]</span>
pytest/test_special_assert.py <span class="pytest-bad">❄️                                                                               [ 63%]</span>
pytest/test_stacked_parameterization.py <span class="pytest-good">🎃 🎃 🎃 🎃 🎃 🎃 </span><span class="pytest-bad">❄️ ❄️ ❄️                                                [ 90%]</span>
pytest/test_xfail.py <span class="pytest-good">🎃 </span><span class="pytest-warn">🍂 </span><span class="pytest-bad">❄️                                                                                   [100%]</span>
====================================================== ERRORS =======================================================
                                                  ...
<span class="pytest-bad">FAILED ❄️ </span> pytest/test_xfail.py::<span class="pytest-ok">test_xpass</span>
<span class="pytest-bad">ERROR 🥧 </span> pytest/test_classes.py::<span class="pytest-ok">TestClass::test_method</span> - NameError: name 'generate_expensive_global' is not defined
</tt></pre>
<pre class="fragment nospace-fragment fade-in" data-fragment-index="1"
    style="background-color:#2E3436; color: #fff; padding: 0.75em;"
>
$ pytest
<b>Test session starts (platform: linux, Python 3.11.8, pytest 8.2.0, pytest-sugar 1.0.0)</b>
plugins: cov-5.0.0, pumpkin-spice-0.1.0, subtests-0.12.1, sugar-1.0.0, hypothesis-6.100.2
<b>collected 2096 items / 1278 deselected / 818 selected                          </b>

 <font color="#06989A">tests/</font>test_easter.py <font color="#10BA13">✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓</font>  <font color="#10BA13">5% </font><span style="background-color:#2E3436"><font color="#10BA13">▌         </font></span>
                      <font color="#10BA13">✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓</font> <font color="#10BA13">11% </font><span style="background-color:#2E3436"><font color="#10BA13">█▏        </font></span>
                      <font color="#10BA13">✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓</font> <font color="#10BA13">16% </font><span style="background-color:#2E3436"><font color="#10BA13">█▋        </font></span>
                      <font color="#10BA13">✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓</font>          <font color="#10BA13">20% </font><span style="background-color:#2E3436"><font color="#10BA13">██        </font></span>
 <font color="#06989A">tests/</font>test_isoparser.py <font color="#10BA13">✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓</font> <font color="#10BA13">25% </font><span style="background-color:#2E3436"><font color="#10BA13">██▌       </font></span>
                         <font color="#10BA13">✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓</font> <font color="#10BA13">30% </font><span style="background-color:#2E3436"><font color="#10BA13">███       </font></span>
                         <font color="#10BA13">✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓</font> <font color="#10BA13">35% </font><span style="background-color:#2E3436"><font color="#10BA13">███▌      </font></span>
                         <font color="#10BA13">✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓</font> <font color="#10BA13">39% </font><span style="background-color:#2E3436"><font color="#10BA13">███▉      </font></span>
                         <font color="#10BA13">✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓</font> <font color="#10BA13">49% </font><span style="background-color:#2E3436"><font color="#10BA13">████▉     </font></span>
                         <font color="#10BA13">✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓</font> <font color="#10BA13">54% </font><span style="background-color:#2E3436"><font color="#10BA13">█████▌    </font></span>
                         <font color="#10BA13">✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓x✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓</font> <font color="#10BA13">64% </font><span style="background-color:#2E3436"><font color="#10BA13">██████▌   </font></span>
                         <font color="#10BA13">✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓</font> <font color="#10BA13">69% </font><span style="background-color:#2E3436"><font color="#10BA13">██████▉   </font></span>
                         <font color="#10BA13">✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓</font> <font color="#10BA13">74% </font><span style="background-color:#2E3436"><font color="#10BA13">███████▍  </font></span>
                         <font color="#10BA13">✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓</font> <font color="#10BA13">83% </font><span style="background-color:#2E3436"><font color="#10BA13">████████▍ </font></span>
                         <font color="#10BA13">✓✓✓✓✓✓✓✓</font>                                 <font color="#10BA13">89% </font><span style="background-color:#2E3436"><font color="#10BA13">████████▉ </font></span>
 <font color="#06989A">tests/</font>test_relativedelta.py <font color="#10BA13">✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓</font> <font color="#10BA13">94% </font><span style="background-color:#2E3436"><font color="#10BA13">█████████▍</font></span>
                             <font color="#10BA13">✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓</font> <font color="#10BA13">98% </font><span style="background-color:#2E3436"><font color="#10BA13">█████████▊</font></span>
                             <font color="#10BA13">✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓</font>                     <font color="#10BA13">100% </font><span style="background-color:#2E3436"><font color="#10BA13">██████████</font></span>

Results (1.32s):
<font color="#10BA13">     817 passed</font>
<font color="#10BA13">       1 xfailed</font>
<font color="#C4A000">    1278 deselected</font>
</pre>
