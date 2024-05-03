def test_special_asserts():
    a = (1, 2, 3)
    assert a is not None       # self.assertIsNot(a, None)
    assert a < (2, 3, 4)       # self.assertLess(a, (2, 3, 4))
    assert len(a) == 4         # self.assertLen(a, 4) - absltest extension
