"""Rotate a list of numbers n positions to right"""

# Pro version
def twist_sequence(l1: list[int], n: int) -> list[int]:
    if not l1:
        return []

    n = n % len(l1)
    return l1[-n:] + l1[:-n]

# 42 student version :)

def twist_sequence2 (l1: list[int], n: int):

    if len(l1) <= 1 or n == 0:
        return l1


    l2 = l1.copy()
    if n > 0:
        for _ in range(n):
            for x in range(0, len(l1)):
                l2[x] = l1[x - 1]
            l1 = l2.copy()
    else:
        for _ in range(abs(n)):
            for x in range(0, len(l1)):
                if x < len(l1) - 1:
                    l2[x] = l1[x + 1]
                else:
                    l2[x] = l1[0]
            l1 = l2.copy()

    return l2


def main():
    test_cases = [
        # Casos básicos
        ([1, 2, 3, 4, 5], 1, [5, 1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),

        # n > len (modular correcto)
        ([1, 2, 3, 4, 5], 7, [4, 5, 1, 2, 3]),   # 7 % 5 = 2
        ([1, 2, 3], 100, [3, 1, 2]),             # 100 % 3 = 1

        # n = 0
        ([1, 2, 3], 0, [1, 2, 3]),

        # lista vacía
        ([], 3, []),

        # lista tamaño 1
        ([42], 10, [42]),

        # negativos → equivalen a izquierda pero normalizados modularmente
        ([1, 2, 3, 4, 5], -1, [2, 3, 4, 5, 1]),
        ([1, 2, 3, 4, 5], -2, [3, 4, 5, 1, 2]),

        # repetidos
        ([1, 1, 1, 1], 3, [1, 1, 1, 1]),

        # números negativos
        ([-1, -2, -3, -4], 1, [-4, -1, -2, -3]),

        # mezcla
        ([10, -5, 7, 3, 0], 3, [7, 3, 0, 10, -5]),
    ]

    # Caso grande (performance)
    big = list(range(100000))
    expected_big = big[-3:] + big[:-3]
    test_cases.append((big, 3, expected_big))

    passed = 0

    for i, (lst, n, expected) in enumerate(test_cases, 1):
        result = twist_sequence(lst.copy(), n)

        if result == expected:
            passed += 1
        else:
            print(f"❌ Test {i} FAILED")
            print(f"Input (first 20): {lst[:20]}")
            print(f"n = {n}")
            print(f"Expected (first 20): {expected[:20]}")
            print(f"Got (first 20): {result[:20]}")
            print()

    print(f"\n✅ Passed {passed}/{len(test_cases)} tests")


if __name__ == "__main__":
    main()