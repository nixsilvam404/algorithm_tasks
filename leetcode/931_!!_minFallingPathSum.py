# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
# A falling path starts at any element in the first row and chooses the element in the next row that 
# is either directly below or diagonally left/right. Specifically, the next element from 
# position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

def minFallingPathSum(matrix: list[list[int]]): # -> int:
    rows, cols = len(matrix)

    for r in range(1, rows):
        for c in range(cols):
            min_above = matrix[r - 1][c]
            if c > 0:
                min_above = min(min_above, matrix[r - 1][c - 1])
            if c < cols - 1:
                min_above = min(min_above, matrix[r - 1][c + 1])
            matrix[r][c] += min_above

    return min(matrix[-1])


# this is not my solution, need to solve by myself

print(minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))