"""counting how many secuences of consecutive digits are in a string"""


def patern_tracker(s: str) -> int:

    numbers = "0123456789"
    # for n in numbers:
    #     s.replace(n, "0")

    total = 0

    if len(s) <= 1:
        return 0

    i = 1
    while i < len(s):
        if s[i] in numbers and s[i-1] in numbers:
            total = total + 1
            while i < len(s) and s[i] in numbers:
                i += 1
        i += 1

    return total

str = "11opifdsa9sfd8sfd8909fsadsdafdfsa09sdfa90sdf09sdaf89sad0f77"
print(patern_tracker(str))
