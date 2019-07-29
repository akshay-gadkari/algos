""" 1.6 String Compression: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string 'aabcccccaaa' would become 'a2b1c5a3'. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a-z). """


s1 = 'aabcccccaaa'
# def compression(s1):
#     s2 = ''
#     count = 0
#     for i in range(len(s1)):
#         # if not s1[i-1]:
#         #     count += 1
#         #     print('none')
#         if i == 0:
#             s2 = s1[i]
#             # count += 1
#         if s1[i] == s1[i-1]:
#             count += 1
#             print(count, str(s1[i]))
#         if s1[i] != s1[i-1]:
#             s2 = s2 + s1[i] + str(count)
#             count = 0
#     if len(s2) >= len(s1):
#         print(s1)
#     print(s2)
#     return
# compression(s1)


def compress(s1):
    compressed = ""
    curr_char = s1[0]
    curr_count = 1
    for i in xrange(1, len(s1)):
        if s1[i] == curr_char:
            curr_count += 1
        else:
            compressed += curr_char
            compressed += str(curr_count)
            curr_char = s1[i]
            curr_count = 1
    compressed += curr_char 
    compressed += str(curr_count)
    print(compressed)
    return compressed
compress(s1)
