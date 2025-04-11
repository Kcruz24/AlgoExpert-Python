# O(N * M) Time | O(N * M)
def transposeMatrix(matrix):
    transposed = []
    row_length = len(matrix)
    col_length = len(matrix[0])
    for col in range(col_length):
        new_row = []
        for row in range(row_length):
            new_row.append(matrix[row][col])
        transposed.append(new_row)

    return transposed

if __name__ == '__main__':
    test = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

    print(transposeMatrix(test))