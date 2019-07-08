def findDiagonalOrder(matrix):
    l = [[i, j] for i in range(len(matrix)) for j in range(len(matrix[0]))]
    l.sort(key=lambda x: float(x[0] + x[1]) - float(x[(x[0] + x[1]) % 2]) * 0.00000001)
    print(len(matrix),len(matrix and matrix[0]))
    return [matrix[x][y] for [x, y] in l]


# def findDiagonalOrder(matrix):
#     m, n = len(matrix), len(matrix and matrix[0])
#     return [matrix[i][d-i]
#             for d in range(m+n-1)
#             for i in range(max(0, d-n+1), min(d+1, m))[::d%2*2-1]]


if __name__ == '__main__':
    # a = [[1,2,3],[4,5,6],[7,8,9]]
    a = [[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12]]
    print(findDiagonalOrder(a))
