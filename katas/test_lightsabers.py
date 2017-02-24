"""Test lightsabers.py."""
from lightsabers import how_many_lightsabers_do_you_own


def test_lightsabers():
    """Test howManyLightSabersDoYouOwn func."""
    assert how_many_lightsabers_do_you_own("Zach") == 18
    assert how_many_lightsabers_do_you_own() == 0
    assert how_many_lightsabers_do_you_own("zach") == 0
