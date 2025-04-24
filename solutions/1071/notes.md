# Notes

## Task
For two strings `s` and `t`, we say "`t` divides `s`" if and only if `s = t + t + t + ... + t + t` (i.e., `t` is concatenated with itself one or more times).

Given two strings `str1` and `str2`, return the largest string `x` such that `x` divides both `str1` and `str2`.



Example 1:
```
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
```
Example 2:
```
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
```
Example 3:
```
Input: str1 = "LEET", str2 = "CODE"
Output: ""
```


Constraints:

    1 <= str1.length, str2.length <= 1000
    str1 and str2 consist of English uppercase letters.

## Tips

Since both strings contains multiples of the identical segment base, their concatenation must be consistent, regardless of the order (str1 + str2 = str2 + str1)

It is kinda clear that len(gcd substring) can't be bigger/smaller than gcd(len(str1), len(str2))
