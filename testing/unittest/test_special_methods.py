import unittest

class Tests(unittest.TestCase):
    def test_special_asserts(self):
        a = (1, 2, 3)
        self.assertIsNot(a, None)
        self.assertLess(a, (2, 3, 4))
        self.assertEqual(len(a), 4)
