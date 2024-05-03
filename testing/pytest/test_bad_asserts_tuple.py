def test_bad_assert():
    a = 1
    assert (
        a == 2,
        "My very long error message doesn't fit on one line, gotta break it up"
    )
