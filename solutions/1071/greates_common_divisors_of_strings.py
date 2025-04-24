import math

class Solution:
    # strings should have gcd != 1
    # if current_gcd is devisor than it should be a prefix for both strings
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        len_1 = len(str1)
        len_2 = len(str2)

        gcd_base = math.gcd(len_1, len_2)
        return str1[:gcd_base]

if __name__ == "__main__":
    solver = Solution()

    tests = [
        ("ABCABC", "ABC"),
        ("ABABAB", "ABAB"),
        ("LEET", "CODE")
    ]

    for test_case in tests:
        solution = solver.gcdOfStrings(*test_case)
        print(f"str1 is: '{test_case[0]}'")
        print(f"str2 is: '{test_case[1]}'")
        print(f"gcd is: '{solution}'")
        print()
