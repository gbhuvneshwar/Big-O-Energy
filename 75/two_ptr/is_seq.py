"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string 
by deleting some (can be none) of the characters without disturbing the relative
positions of the remaining characters. (i.e., "ace" is a subsequence of 
"abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
"""

def is_subsequence(s: str, t: str) -> bool:
    s_len, t_len = len(s), len(t)
    if s_len == 0:
        return True
    if t_len == 0:
        return False

    s_ptr, t_ptr = 0, 0

    while s_ptr < s_len and t_ptr < t_len:
        if s[s_ptr] == t[t_ptr]:
            s_ptr += 1
        t_ptr += 1

    return s_ptr == s_len





