"""Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. Input to the function is guaranteed to be a single string.

Examples of valid inputs: 1.2.3.4 123.45.67.89

Examples of invalid inputs: 1.2.3 1.2.3.4.5 123.456.78.90 123.045.067.089."""


def is_valid_IP(strng):
    split = strng.split('.')
    for i in split:
        if not i.isdigit():
            return False
        if len(i) > 3 or len(i) < 1:
            return False
        if i[0] == '0' or not i[0].isdigit():
            return False
        if int(i) > 255 or int(i) < 1:
            return False
    if len(split) != 4:
        return False
    return True