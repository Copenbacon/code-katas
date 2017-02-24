"""Playing Banjo from Codewars."""


def are_you_playing_banjo(name):
    """Implement me."""
    if name[0].lower() == 'r':
        name += ' plays banjo'
    else:
        name += ' does not play banjo'
    return name
