import unittest
import hypothesis
from hypothesis import strategies as st

class ExampleHypothesisTest(unittest.TestCase):
    @hypothesis.given(dt_1=st.datetimes(timezones=st.timezones()),
                      dt_2=st.datetimes(timezones=st.timezones()))
    def test_timestamp(self, dt_1, dt_2):
        ts2 = dt_2.timestamp()
        dt_rt = (dt_1 + (dt_2 - dt_1))
        self.assertEqual(ts2, dt_rt.timestamp())
