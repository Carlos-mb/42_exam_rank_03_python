"""You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise."""


def main(s: str):

    salida: str = ""

    for letter in s:
        if letter in "[{()}]":
            salida += letter

    while '()' in salida or '{}' in salida or '[]' in salida:
        salida = salida.replace('()', '')
        salida = salida.replace('{}', '')
        salida = salida.replace('[]', '')

    return salida == ''

# print (main("dasfdasf"))
# print (main("das{fdas}f"))
# print (main("das{fd]as}f"))