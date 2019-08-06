# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

# This is case sensitive, for example "Aa" is not considered a palindrome here.

# Note:
# Assume the length of given string will not exceed 1,010.

# Example:

# Input:
# "abccccdd"

# Output:
# 7

# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.


s = 'racecar'
# class Solution:
def longestPalindrome(s):
    d = dict()
    odds = 0
    for i in s:
        if i in d:
            d[i] += 1
        else: d[i] = 1
#    d = [s.count(i) for i in s]
    for i in d:
        if d[i] % 2 != 0:
            odds += 1
    if odds > 1:
        print(len(s) - odds + 1)
    else:
        print(len(s))
    
longestPalindrome(s)
