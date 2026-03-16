"""Check if two strings has the same characters in the same frequence"""


def permutation_checker(s1: str, s2: str):
    return sorted(s1) == sorted(s2)


print(permutation_checker("ldkfjeu", "ldfjeuk"))
print(permutation_checker("ldkfjeu", "ldfjeuk "))
