"""You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise."""


def main(self, s: str):

    while '()' in s or '{}' in s or '[]' in s:
        s = s.replace('()', '')
        s = s.replace('{}', '')
        s = s.replace('[]', '')

    return s == ''

