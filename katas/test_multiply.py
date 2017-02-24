"""There was no test file for the Multiply Kata, so I made some of my own."""


def test_multiply():
    """Test the multiply function from Codewars."""
    from multiply import multiply
    assert multiply(6, 7) == 42
    assert multiply(23, 2) is not 40
