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