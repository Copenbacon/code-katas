"""Testing banjo.py from Codewars."""
from banjo import are_you_playing_banjo


def test_banjo():
    """Test the main function from banjo.py."""
    assert are_you_playing_banjo("martin") == "martin does not play banjo"
    assert are_you_playing_banjo("Rikke") == "Rikke plays banjo"
    assert are_you_playing_banjo("Adam"), "Adam does not play banjo"
    assert are_you_playing_banjo("Paul"), "Paul does not play banjo"
    assert are_you_playing_banjo("Ringo"), "Ringo plays banjo"
    assert are_you_playing_banjo("bravo"), "bravo does not play banjo"
    assert are_you_playing_banjo("rolf"), "rolf plays banjo"
