"""Write a function called validParentheses that takes a string of parentheses, and determines if the order of the parentheses is valid. validParentheses should return true if the string is valid, and false if it's invalid.

Examples: 
validParentheses( "()" ) => returns true 
validParentheses( ")(()))" ) => returns false 
validParentheses( "(" ) => returns false 
validParentheses( "(())((()())())" ) => returns true 

All input strings will be nonempty, and will only consist of open parentheses '(' and/or closed parentheses ')'"""


def valid_parentheses(string):
    matches = []
    for item in string:
        if item == "(":
            matches.append("(")
        if item == ")":
            try:
                matches.pop() 
            except IndexError:
                return False
    if matches:
        return False
    return True