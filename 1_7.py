""" 1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place? """

matrix = [[1,  2,  3,  4 ],
         [5,  6,  7,  8 ],
         [9,  10, 11, 12 ],
         [13, 14, 15, 16 ]]

def rotate(m):
    m2 = []
    for i in range(len(m)):
        res = []
        for j in range(len(m)):
            res.append(m[j][i])
        m2.append(res[::-1])
    print(m2)
    return
rotate(matrix)
