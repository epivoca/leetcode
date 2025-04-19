class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_len = len(word1)
        word2_len = len(word2)

        if word1_len == word2_len:
            return self._merge_equal_part(word1, word2)


        if word1_len < word2_len:
            merged_word = self._merge_equal_part(word1, word2[:word1_len])
            return merged_word + word2[word1_len:]

        merged_word = self._merge_equal_part(word1[:word2_len], word2)
        return merged_word + word1[word2_len:]


    @staticmethod
    def _merge_equal_part(word1: str, word2: str) -> str:
        assert len(word1) == len(word2)

        merged_word = ""
        for i in range(len(word1)):
            merged_word += word1[i] + word2[i]

        return merged_word


if __name__ == "__main__":
    solver = Solution()

    tests = [
        ("abc", "pqr"),
        ("ab", "pqrs"),
        ("abcd", "pq")
    ]

    for test_case in tests:
        solution = solver.mergeAlternately(*test_case)
        print(f"word1 is: '{test_case[0]}'")
        print(f"word2 is: '{test_case[1]}'")
        print(f"solution is: '{solution}'")
        print()
