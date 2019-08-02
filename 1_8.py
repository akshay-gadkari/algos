""" 1.8 Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0. """

m = [[1,  2,  3,  4 ],
     [5,  6,  0,  8 ],
     [9,  10, 11, 12 ]]

# def zero_matrix(m):
#     m2 = []
#     list_of_zeroes = []
#     zeroes = 0
#     rowlen = len(m[0])
#     for i in range(len(m)):
#         # print('i', i)
#         for j in range(len(m[0])):
#             # print('j is', j)
#             if m[i][j] == 0:
#                 print(m[i][j], i, j)
#                 m2.append(i)
#                 m2.append(j)
#                 list_of_zeroes.append(m2)
#                 print('m[i]', m[i])
#                 m2 = []
#     print(m)
#     row = list_of_zeroes[0][0]
#         m[row] = []
#     print(list_of_zeroes[0][0])

# def zero_matrix(m):
#     for i in range(len(m)):
#         if 0 in m[i]:
#             print(0, "in row", i)
#     return

def locate_zero_rows(matrix: list) -> list:
    """Given an NxM matrix find the rows that contain a zero."""
    return [i for i, row in enumerate(matrix) if not all(row)]

zero_matrix(m)
