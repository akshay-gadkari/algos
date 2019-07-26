""" 1.5 One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away. """

s1 = "abc"
s2 = "cbd"
def one_away(s1, s2):
    if s1 == s2:
        print(f'zero away')
        return
    if len(s1) == len(s2):
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
        if count == 1:
            print('one away')
            return
        if count > 1:
            print('over 1 away')
            return
    if len(s1) == len(s2) + 1:
        for i in range(len(s1)):
            if (s1[:i] + s1[i + 1:]) == s2:
                print('one away')
                return
            else:
                print('over 1 away')
                return
    if len(s2) == len(s1) + 1:
        for i in range(len(s2)):
            if (s2[:i] + s2[i+1:]) == s1:
                print('one away')
                return
            else:
                print('over 1 away')
                return
    else:
        print("over 1 away")
            

one_away(s1, s2)
