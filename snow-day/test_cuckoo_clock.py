"""Testing cuckoo clock module."""
from cuckoo_clock import fizz_buzz_cuckoo_clock


def test_basics():
    """Basic times tests."""
    assert fizz_buzz_cuckoo_clock("13:34") == "tick"
    assert fizz_buzz_cuckoo_clock("21:00") == "Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo"
    assert fizz_buzz_cuckoo_clock("11:15") == "Fizz Buzz"
    assert fizz_buzz_cuckoo_clock("03:03") == "Fizz"
    assert fizz_buzz_cuckoo_clock("14:30") == "Cuckoo"
    assert fizz_buzz_cuckoo_clock("08:55") == "Buzz"
    assert fizz_buzz_cuckoo_clock("00:00") == "Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo"
    assert fizz_buzz_cuckoo_clock("12:00") == "Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo"

"""Not sure why this stuff below doesn't work, kept getting fixture 'time' not found error in pytest. So I'm commenting it out."""

# def test_my_fizz_buzz_cuckoo_clock(time):
#     """Random times tests."""
#     import random
#     hours, minutes = map(int, time.split(":"))
#     sounds = {0: " ".join(["Cuckoo"] * (hours % 12 or 12)), 15: "Fizz Buzz", 30: "Cuckoo", 45: "Fizz Buzz"}
#     if minutes in sounds:
#         return sounds[minutes]
#     return "Fizz" if minutes % 3 == 0 else "Buzz" if minutes % 5 == 0 else "tick"
#     # first, I want to be sure that 0, 15, 30, and 45 do get included regardless
#     # of whatever other completely random numbers come up in subsequent tests
#     for quarter in [0, 15, 30, 45]:
#         quarter_test = "{:02}:{:02}".format(random.randint(0, 23), quarter)
#         expected, actual = test_my_fizz_buzz_cuckoo_clock(quarter_test), fizz_buzz_cuckoo_clock(quarter_test)
#         assert actual == expected
#     # and some totally-random tests
#     for i in range(40):
#         random_test = "{:02}:{:02}".format(random.randint(0, 23), random.randint(0, 59))
#         expected, actual = test_my_fizz_buzz_cuckoo_clock(random_test), fizz_buzz_cuckoo_clock(random_test)
#         assert actual == expected
