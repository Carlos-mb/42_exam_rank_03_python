"""You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise."""


class Solution:
    def sameopenclose(self, s:str):
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

    def isperfect(self, s: str, i):
        par = 0
        ll = 0
        cor = 0
        for l in s[i+1:]:  # from current pos until the end
            if s[i] == "(" and l == ")":  # if finished with no errors
                return par + ll + cor == 0
            if s[i] == "[" and l == "]":  # if finished with no errors
                return par + ll + cor == 0
            if s[i] == "{" and l == "}":  # if finished with no errors
                return par + ll + cor == 0
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

    def isValid(self, s: str) -> bool:
        if not self.sameopenclose(s):
            return False

        for i in range(len(s) - 1):
            if s[i] in "([{":  # for each open
                if not self.isperfect(s, i):
                    return False
        return True


def main():
    sol = Solution()
    print(sol.isValid("[]"))  # True
    print(sol.isValid("[()]"))  # True
    print(sol.isValid("[(])"))  # False
    print(sol.isValid("[444(s{{{}}}s)s[s]"))  # False


if __name__ == "__main__":
    main()
