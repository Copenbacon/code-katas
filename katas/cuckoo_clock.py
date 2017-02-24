"""Make a cuckoo clock."""


def fizz_buzz_cuckoo_clock(time):
    """Cuckoo Clock Rules."""
    three_time = "Fizz"
    five_time = "Buzz"
    on_the_hour = ["Cuckoo"]
    every_minute = "tick"
    current_hour = int(time[0:2])
    current_minutes = int(time[3:])
    if current_minutes == 0:
        if current_hour > 12:
            return ' '.join(on_the_hour * (current_hour - 12))
        elif current_hour == 0:
            return ' '.join(on_the_hour * 12)
        return ' '.join(on_the_hour * current_hour)
    elif current_minutes == 30:
        return ' '.join(on_the_hour)
    elif current_minutes % 3 == 0 and current_minutes % 5 == 0:
        return three_time + ' ' + five_time
    elif current_minutes % 5 == 0:
        return five_time
    elif current_minutes % 3 == 0:
        return three_time
    else:
        return every_minute
