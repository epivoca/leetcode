# Notes

## Task

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

### Example 1:

```
Input: s = "IceCreAm"
Output: "AceCreIm"
```

### Explanation:

The vowels in s are `['I', 'e', 'e', 'A']`. On reversing the vowels, s becomes "AceCreIm".

### Example 2:

```
Input: s = "leetcode"
Output: "leotcede"
```

### Constraints:
```
1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
```

## Alternative implementation

That one from solutions looks prettier than mine:
```python
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
        lst = []
        for char in s:
            if char in vowels:
                lst.append(char)
        result = ""
        for char in s:
            if char in vowels:
                result += lst[-1]
                lst.pop(-1)
            else:
                result += char
        return result
```
