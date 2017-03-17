"""Write a function called validBraces that takes a string of braces, and determines if the order of the braces is valid. validBraces should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces four new characters. Open and closed brackets, and open and closed curly braces. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of open parentheses '(' , closed parentheses ')', open brackets '[', closed brackets ']', open curly braces '{' and closed curly braces '}'.

What is considered Valid? A string of braces is considered valid if all braces are matched with the correct brace. 
For example:
'(){}[]' and '([{}])' would be considered valid, while '(}', '[(])', and '[({})](]' would be considered invalid.

Examples: 
validBraces( "(){}[]" ) => returns true 
validBraces( "(}" ) => returns false 
validBraces( "[(])" ) => returns false 
validBraces( "([{}])" ) => returns true"""


def validBraces(string):
    mtch_counter = 0
    key_chart = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    if len(string) % 2 != 0:
        return False
    halfling = len(string) // 2
    for idx, item in enumerate(string[0:halfling]):
        if item not in key_chart:
            continue
        if key_chart[item] == string[len(string) - 1 - idx]:
            mtch_counter += 1
        elif idx % 2 == 0:
            if key_chart[item] == string[idx + 1]:
                mtch_counter += 2
    if mtch_counter == len(string) // 2:
        return True
    return False