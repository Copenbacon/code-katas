"""Return a list split by multiple delimiters."""


def multiple_split(string, delimiters=[]):
    """Split a string into a list by mult delimiters."""
    if delimiters == []:
        return [string] if string else []
    for x in delimiters:
        string = string.replace(x, ' ')
    return string.split()
