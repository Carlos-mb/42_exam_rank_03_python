"""Receive 2 strings. For each character in each string you have con check
that it exist in the other string in the same frequency.

I can't remember all the subject, but they give a 5 lines explantion of what to check:

Any letter in one string has to exist the same times in the other string in any order
Spaces are considered an character
It is case sensitive"""


def permutation_checker(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)
