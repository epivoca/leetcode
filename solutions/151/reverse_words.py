class Solution(object):
    def reverseWords(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        words.reverse()
        return " ".join(words)
