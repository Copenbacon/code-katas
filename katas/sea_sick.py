"""Testing change in a string of ~ and _."""


def sea_sick(sea):
    """Testing change."""
    if (sea.count("~_") + sea.count("_~")) > 0.2 * len(sea):
        return "Throw Up"
    else:
        return "No Problem"
