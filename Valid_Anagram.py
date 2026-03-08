"""Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
"""
class Solution:
    def isValid(self, s: str) -> bool:
        par = 0
        ll = 0
        cor = 0
        for l in s:
            if l == "(":
               par += 1
            elif l == ")":
                par -= 1
            elif l == "{":
                ll += 1
            elif l == "}":
                ll -= 1
            elif l == "[":
                cor += 1
            elif l == "]":
                cor -= 1
            if par * ll * cor < 0:
                return False
        return True
