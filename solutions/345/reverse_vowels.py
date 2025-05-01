
class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """

        left_ind = 0
        right_ind = len(s) - 1

        vowels = "aeiouAEIOU"
        s_list = list(s)

        while left_ind < right_ind:
            while s_list[left_ind] not in vowels and left_ind < right_ind:
                left_ind += 1

            while s_list[right_ind] not in vowels and right_ind > left_ind:
                right_ind -= 1

            if left_ind >= right_ind:
                break

            s_list[left_ind], s_list[right_ind] = s_list[right_ind], s_list[left_ind]
            left_ind += 1
            right_ind -= 1

        return "".join(s_list)

if __name__ == "__main__":
    solver = Solution()

    tests = [
        "IceCreAm",
        "leetcode",
        ".,"
    ]

    for test_case in tests:
        solution = solver.reverseVowels(test_case)
        print(f"input string: '{test_case}'")
        print(f"result: '{solution}'")
        print()
