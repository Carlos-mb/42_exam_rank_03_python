"""Generates an encryption of a string by adding n to its ASCII"""


def whisper_cipher(s: str, n: int):

    output = ""
    n = n % 26

    for letter in s:
        if (ord(letter) >= ord("a") and ord(letter) <= ord("z")):
            nchar = (ord(letter) + n)
            while nchar > ord("z"):
                nchar = nchar - ord("z") + ord("a") - 1
            output += chr(nchar)
        elif (ord(letter) >= ord("A") and ord(letter) <= ord("Z")):
            nchar = (ord(letter) + n)
            while nchar > ord("Z"):
                nchar = nchar - ord("Z") + ord("A") - 1
            output += chr(nchar)
        else:
            output = output + letter

    return output


def main():
    tests = [
        ("abc", 1, "bcd"),           # caso básico
        ("xyz", 2, "zab"),           # wrap minúsculas
        ("XYZ", 3, "ABC"),           # wrap mayúsculas
        ("aAzZ", 301, "pPoO"),       # n grande (301 % 26 = 15)
        ("Hello, World!", 5, "Mjqqt, Btwqi!")  # con símbolos
    ]

    passed = 0

    for i, (s, n, expected) in enumerate(tests, 1):
        result = whisper_cipher(s, n)
        if result == expected:
            passed += 1
        else:
            print(f"❌ Test {i} FAILED")
            print(f"Input: {s}, n={n}")
            print(f"Expected: {expected}")
            print(f"Got: {result}")
            print()

    print(f"✅ Passed {passed}/{len(tests)} tests")


if __name__ == "__main__":
    main()
