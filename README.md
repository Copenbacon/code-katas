# code-katas

##Current Coverage
```
---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                                Stmts   Miss  Cover   Missing
-----------------------------------------------------------------
katas/IP_validation.py                 14      1    93%   14
katas/anagrams.py                       7      0   100%
katas/baker.py                          9      0   100%
katas/banjo.py                          5      0   100%
katas/convert_array.py                  7      0   100%
katas/cuckoo_clock.py                  22      0   100%
katas/debug_string_add.py               8      0   100%
katas/dinner_plans.py                  10      0   100%
katas/dll.py                           70     32    54%   37-38, 40, 49-50, 56, 78-85, 89-96, 100-110
katas/dup_encoder.py                    8      0   100%
katas/flatten.py                        7      0   100%
katas/lightsabers.py                    4      0   100%
katas/mult_delimiters.py                6      0   100%
katas/multiply.py                       2      0   100%
katas/nonrepeating_letter.py            5      0   100%
katas/perfectpower.py                  11      0   100%
katas/prime.py                         11      0   100%
katas/proper_parenthetics.py           12      0   100%
katas/sea_sick.py                       4      0   100%
katas/sort_cards.py                    28      0   100%
katas/sum_series.py                     5      0   100%
katas/test_anagrams.py                  5      0   100%
katas/test_baker.py                     7      0   100%
katas/test_banjo.py                     9      0   100%
katas/test_convert_array.py            13      0   100%
katas/test_cuckoo_clock.py             26      0   100%
katas/test_debug_string_add.py          5      0   100%
katas/test_dinner_plans.py             20      0   100%
katas/test_dup_encoder.py              14      0   100%
katas/test_flatten.py                  23      0   100%
katas/test_ip_validation.py             8      0   100%
katas/test_lightsabers.py               5      0   100%
katas/test_mult_delimiters.py          11      0   100%
katas/test_multiply.py                  4      0   100%
katas/test_nonrepeating_letter.py      12      0   100%
katas/test_perfectpower.py             24      9    63%   30-39
katas/test_prime.py                     5      0   100%
katas/test_proper_parenthetics.py       5      0   100%
katas/test_sea_sick.py                 14      0   100%
katas/test_sort_cards.py               16      0   100%
katas/test_sum_terms.py                21      0   100%
katas/test_valid_braces.py              8      0   100%
katas/test_valid_parentheses.py        16      0   100%
katas/valid_braces.py                  17      0   100%
katas/valid_parentheses.py             13      0   100%
-----------------------------------------------------------------
TOTAL                                 556     42    92%


========================== 111 passed in 0.48 seconds 

----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                                Stmts   Miss  Cover   Missing
-----------------------------------------------------------------
katas/IP_validation.py                 14      1    93%   14
katas/anagrams.py                       7      0   100%
katas/baker.py                          9      0   100%
katas/banjo.py                          5      0   100%
katas/convert_array.py                  7      0   100%
katas/cuckoo_clock.py                  22      0   100%
katas/debug_string_add.py               8      0   100%
katas/dinner_plans.py                  10      0   100%
katas/dll.py                           70     32    54%   37-38, 40, 49-50, 56, 78-85, 89-96, 100-110
katas/dup_encoder.py                    8      0   100%
katas/flatten.py                        7      0   100%
katas/lightsabers.py                    4      0   100%
katas/mult_delimiters.py                6      0   100%
katas/multiply.py                       2      0   100%
katas/nonrepeating_letter.py            5      0   100%
katas/perfectpower.py                  11      0   100%
katas/prime.py                         11      0   100%
katas/proper_parenthetics.py           12      0   100%
katas/sea_sick.py                       4      0   100%
katas/sort_cards.py                    28      0   100%
katas/sum_series.py                     5      0   100%
katas/test_anagrams.py                  5      0   100%
katas/test_baker.py                     7      0   100%
katas/test_banjo.py                     9      0   100%
katas/test_convert_array.py            13      0   100%
katas/test_cuckoo_clock.py             26      0   100%
katas/test_debug_string_add.py          5      0   100%
katas/test_dinner_plans.py             20      0   100%
katas/test_dup_encoder.py              14      0   100%
katas/test_flatten.py                  23      0   100%
katas/test_ip_validation.py             8      0   100%
katas/test_lightsabers.py               5      0   100%
katas/test_mult_delimiters.py          11      0   100%
katas/test_multiply.py                  4      0   100%
katas/test_nonrepeating_letter.py      12      0   100%
katas/test_perfectpower.py             24      2    92%   36-37
katas/test_prime.py                     5      0   100%
katas/test_proper_parenthetics.py       5      0   100%
katas/test_sea_sick.py                 14      0   100%
katas/test_sort_cards.py               16      0   100%
katas/test_sum_terms.py                21      0   100%
katas/test_valid_braces.py              8      0   100%
katas/test_valid_parentheses.py        16      0   100%
katas/valid_braces.py                  17      0   100%
katas/valid_parentheses.py             13      0   100%
-----------------------------------------------------------------
TOTAL                                 556     35    94%


========================== 111 passed in 0.62 seconds
```


### A collection of my solutions for Code Katas from CodeWars.com

##Valid Braces
### 4 kyu
####-Module: valid_braces.py
####-Tests: test_valid_braces.py
####-Link: https://www.codewars.com/kata/valid-braces/train/python
```python
"""Nice solve by herringjob."""
def validBraces(s):
  while '{}' in s or '()' in s or '[]' in s:
      s=s.replace('{}','')
      s=s.replace('[]','')
      s=s.replace('()','')
  return s==''
```

##Pete, the baker
### 5 kyu
####-Module: baker.py
####-Tests: test_baker.py
####-Link: https://www.codewars.com/kata/pete-the-baker/train/python
```python
"""Great one liner from jerb, Ninjailbreak, sweettuse."""
def cakes(recipe, available):
  return min(available.get(k, 0)/recipe[k] for k in recipe)
```

##Valid Parentheses
### 5 kyu
####-Module: valid_parentheses.py
####-Tests: test_valid_parentheses.py
####-Link: https://www.codewars.com/kata/valid-parentheses/train/python
```python
"""Interesting solve by albarralnunez, oshinjose, alanmathew671"""
def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False"
```

##IP Validation
### 4 kyu
####-Module: IP_validation.py
####-Tests: test_ip_validation.py
####-Link:https://www.codewars.com/kata/ip-validation/train/python
```python
"""List comprehension solve by pavel.koshev"""
import re
def is_valid_IP(strng):
    return bool(re.match(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}(?=$)',strng))
```

##First Non-Repeating Letter
###5 kyu
####-Module: nonrepeating_letter.py
####-Tests: test_nonrepeating_letter.py
####-Link: https://www.codewars.com/kata/first-non-repeating-letter/train/python
```python
"""List comprehension solve by alm8735"""

def first_non_repeating_letter(string):
    singles = [i for i in string if string.lower().count(i.lower()) == 1]
    return singles[0] if singles else ''
```

##Where my Anagrams at?
###5 kyu
####-Module: anagrams.py
####-Tests: test_anagrams.py
####-Link: https://www.codewars.com/kata/where-my-anagrams-at/train/python
```python
"""Great list comprehension solution by sandbochs, Dru7-BY, fandogh"""
def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]
```

##Perfect Powers
###5 kyu
####-Module: perfectpower.py
####-Tests: test_perfectpower.py
####-Link: https://www.codewars.com/kata/whats-a-perfect-power-anyway/train/python
```python
"""I really liked this solution by fanzen190."""

from math import sqrt, log
def isPP(n):
    for m in range(2, int(sqrt(n)) + 1):
        k = round(log(n, m))
        if m ** k == n:
            return [m, k]

    return None
```

##Is a Number Prime?
###6 kyu
####-Module: prime.py
####-Tests: test_prime.py
####-Link: https://www.codewars.com/kata/is-a-number-prime/train/python
```python
"""The solution by nevin and shig was pretty interesting."""
def is_prime(num):
    return num > 1 and not any(num % n == 0 for n in range(2,num))
```

##Duplicate Encoder
###6 kyu
####-Module: dup_encoder.py
####-Tests: test_dup_encoder.py
####-Link: https://www.codewars.com/kata/duplicate-encoder/train/python
```python
"""This was the solution by SevenEcks, I like that it is O(n) over O(n^2):"""
#This solution is O(n) instead of O(n^2) like the methods that use .count()
#because .count() is O(n) and it's being used within an O(n) method.
#The space complexiety is increased with this method.
import collections
def duplicate_encode(word):
    new_string = ''
    word = word.lower()
    #more info on defaultdict and when to use it here:
    #http://stackoverflow.com/questions/991350/counting-repeated-characters-in-a-string-in-python
    d = collections.defaultdict(int)
    for c in word:
        d[c] += 1
    for c in word:
        new_string = new_string + ('(' if d[c] == 1 else ')')
    return new_string
```

##Sort Cards
####-Module: sort_cards.py
####-Tests: test_sort_cards.py
####-Link: https://www.codewars.com/kata/sort-deck-of-cards/train/python
```python
"""This was the solution by zebulan, Unnamed, acaccia, j_codez, Mr.Child, iamchingel."""
def sort_cards(cards):
    return sorted(cards, key="A23456789TJQK".index)
```

##Proper Parenthetics
####-Module: proper_parenthetics.py
####-Tests: test_proper_parenthetics.py
####-Link: https://codefellows.github.io/sea-python-401d5/assignments/proper_parenthetics.html

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

##Sum of the first nth term of Series
##7 kyu
####-Module: sum_series.py
####-Tests: test_sum_terms.py
####-Link: http://www.codewars.com/kata/555eded1ad94b00403000071/solutions/python
```python
"""This was the solution by MMMAAANNN, doctornick5, Slx64."""
def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
```