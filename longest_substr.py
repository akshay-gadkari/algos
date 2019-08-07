# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 

# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

s = 'abcdefgggghijklmnopqrstuvwxyz'
def longest_substr(s):
    s2 = ''
    longest = ''
    for i in range(len(s)):
        if s[i] != s[i-1]:
            s2 = s2 + s[i]
            # print('same')
            #print(s2)
        else:
            if len(s2) < len(longest):
                longest += s2
                s2 = ''
    if len(s2) < len(longest):
        print(s2)
    else:
        print(longest)
    return

longest_substr(s)
