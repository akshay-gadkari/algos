""" 1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words. """

str1 = 'racecar'
def palindrome(s):
    d = dict()
    odds = 0
    for i in s:
        if i in d:
            d[i] += 1
            print(d, d[i])
        else:
            d[i] = 1
            print(d, d[i])
    for i in d:
        if d[i] % 2 != 0:
            odds += 1
            print("odds", odds)
    if odds > 1:
            print('not a palindrome')
    else:
        print('a palindrome')
        

palindrome(str1)
