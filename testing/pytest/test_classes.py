class TestClass:
    @classmethod
    def setup_class(cls):
        """Run when class is initialized."""
        cls.EXPENSIVE_GLOBAL = generate_expensive_global()

    @classmethod
    def teardown_class(cls):
        """Run when class is destroyed."""
        cls.EXPENSIVE_GLOBAL.free_resources()

    def setup_method(self, method):
        """Run before every test method execution."""

    def teardown_method(self, method):
        """Run after every test method execution."""

    def test_method(self):
        """This is a test that is actually run."""
        assert 1 == 1
