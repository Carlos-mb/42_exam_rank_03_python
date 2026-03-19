"""Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.

"""


def isPalindrome(s: str) -> bool:
    s_low = s.lower()

    s2 = ""
    for letter in s_low:
        if letter in "abcdefghijklmnopqrstuwxyz0123456789":
            s2 += letter

    i = -1
    for letter in s2:
        if letter != s2[i]:
            return False
        i -= 1

    return True


def main():
    test_cases = [
        # Vacíos / solo ignorables
        ("", True),
        (" ", True),
        ("!!!", True),
        (".,", True),

        # Longitud 1
        ("a", True),
        ("Z", True),
        ("7", True),
        (".", True),

        # Palíndromos simples
        ("aba", True),
        ("abba", True),
        ("racecar", True),
        ("1221", True),

        # No palíndromos simples
        ("ab", False),
        ("abc", False),
        ("1231", False),

        # Case insensitive
        ("Aa", True),
        ("RaceCar", True),
        ("MadAm", True),

        # Ignorar símbolos
        ("A man, a plan, a canal: Panama", True),
        ("No 'x' in Nixon", True),
        ("Was it a car or a cat I saw?", True),
        ("race a car", False),

        # Letras + números
        ("1a2", False),
        ("1a1", True),
        ("1A@a1", True),
        ("0P", False),

        # Solo ignorables + uno
        ("!!!a!!!", True),
        ("!!!ab!!!", False),

        # Casos tricky clásicos
        ("a.", True),
        (".a", True),
        (".,a", True),

        # Limpieza cambia resultado
        ("ab@a", True),
        ("ab@c", False),
        ("a-b-a", True),

        # Unicode (según spec debería ignorarse o fallar)
        ("áa", False),
        ("ß", True),
        ("😊", True),
    ]

    # Casos grandes (performance)
    large_palindrome = "a" * 100000
    large_near_palindrome = "a" * 50000 + "b" + "a" * 50000

    test_cases.append((large_palindrome, True))
    test_cases.append((large_near_palindrome, True))

    passed = 0

    for i, (s, expected) in enumerate(test_cases, 1):
        result = isPalindrome(s)
        if result == expected:
            passed += 1
        else:
            print(f"❌ Test {i} FAILED")
            print(f"Input: {repr(s[:50])}...")
            print(f"Expected: {expected}, Got: {result}")
            print()

    print(f"\n✅ Passed {passed}/{len(test_cases)} tests")


if __name__ == "__main__":
    main()
