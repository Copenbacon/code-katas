# code-katas


##Multiply
###8 kyu
####-Module: multiply.py
####-Tests: test_multiply.py
####-Link: https://www.codewars.com/kata/50654ddff44f800200000004/train/python
```python
"""This was the solution by nedsociety, Hartrik, monkeydust, webtechalex, Mikhail158, highfestiva and more."""
multiply = lambda a,b: a * b
```

##Banjo
###8 kyu
####-Module: banjo.py
####-Tests: test_banjo.py
####-Link: https://www.codewars.com/kata/53af2b8861023f1d88000832/train/python
```python
"""This was the solution by lechevalier."""
areYouPlayingBanjo=lambda n:n+[" does not play"," plays"][n[0]in'Rr']+" banjo"
```

##Lightsabers
###8 kyu
####-Module: lightsabers.py
####-Tests: test_lightsabers.py
####-Link: https://www.codewars.com/kata/51f9d93b4095e0a7200001b8/solutions/python
```python
"""This was the solution by kylehill, Daniel.Liu, dimrozakis, Jajo, Dokopuffs, andross (plus 145 more warriors)."""
def howManyLightsabersDoYouOwn(name=""):
    return (18 if name=="Zach" else 0)
```

##Digitize
###8 kyu
####-Module: convert_array.py
####-Tests: test_convert_array.py
####-Link: https://www.codewars.com/kata/5583090cbe83f4fd8c000051/solutions/python
```python
"""This was the solution by GiacomoSorbi, narayanswa30663."""
digitize=lambda n: map(int, list(str(n))[::-1])
```

##Noob Debug 1: Fix the string sum!
##7 kyu
####-Module: debug_string_add.py
####-Tests: test_debug_string_add.py
####-Link: https://www.codewars.com/kata/noob-debug-1-fix-the-string-sum/solutions/python/
```python
"""This was the solution by MiraliN, Chris_Rands."""
def add(s1, s2):
    return sum(ord(x) for x in s1+s2)
```

##Flatten Me
##7 kyu
####-Module: flatten.py
####-Tests: test_flatten.py
####-Link: https://www.codewars.com/kata/55a5bef147d6be698b0000cd/solutions/python
```python
"""This was the solution by daddepledge."""
def flatten_me(lst):
    return [v for sub in [e if type(e) == list else [e] for e in lst] for v in sub]
```

##Dinner Plans
##7 kyu
####-Module: dinner_plans.py
####-Tests: test_dinner_plans.py
####-Link: https://www.codewars.com/kata/57212c55b6fa235edc0002a2/solutions/python
```python
"""This was the solution by Mr.Child."""
def common_ground(s1,s2):
    s = s2.split()
    return ' '.join(sorted((x for x in set(s1.split()) if x in s), key=lambda y: s.index(y))) or 'death'
```

##Multiple Delimiters
##7 kyu
####-Module: mult_delimiters.py
####-Tests: test_mult_delimiters.py
####-Link: https://www.codewars.com/kata/575690ee34a34efb37001796/solutions/python
```python
"""This was the solution by anter69."""
from re import split, escape

def multiple_split(string, delimiters=[]):
    return filter(None, split('|'.join(map(escape, delimiters)), string))
```

##Fizz Buzz Cuckoo Clock
##7 kyu
####-Module: cuckoo_clock.py
####-Tests: test_cuckoo_clock.py
####-Link: https://www.codewars.com/kata/58485a43d750d23bad0000e6/solutions/python
```python
"""This was the solution by kjmosher."""
def fizz_buzz_cuckoo_clock(time):
    hours, minutes = map(int, time.split(':'))
    hours = hours - 12 * (hours > 12) or 12
    if not minutes % 30:
        return ' '.join(['Cuckoo'] * (hours if not minutes else 1))
    return ' '.join(('Fizz' * (not minutes % 3), 'Buzz' * (not minutes % 5))).strip() or 'tick'
```

##Sea Sick
##7 kyu
####-Module: sea_sick.py
####-Tests: test_sea_sick.py
####-Link: https://www.codewars.com/kata/57e90bcc97a0592126000064/solutions/python
```python
"""This was the solution by lechevalier."""
sea_sick = lambda s:["No Problem", "Throw Up"][s.count('~_') + s.count('_~')> .2 * len(s)]
```