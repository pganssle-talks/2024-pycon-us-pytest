import unittest

class Tests(unittest.TestCase):
    def test_bad_assert(self):
        a = 1
        self.assertEqual(a, 2)
