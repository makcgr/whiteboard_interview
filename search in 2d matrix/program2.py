from typing import List

def search2D(matrix: List[List[int]], val: int):
    ROWS = len(matrix)
    COLS = len(matrix[0])

    r, c = ROWS - 1, 0 # start from left bottom

    # whle r >= 0 and c < COLS - 1
    # if val == cur: return true
    # if val is less then cur: val can't be in a row, r -= 1
    # else if val is greater than cur: val can't be in a col, col += 1 

    while r >= 0 and c <= COLS - 1:
        if val == matrix[r][c]:
            return True
        elif val < matrix[r][c]:
            r -= 1
        elif val > matrix[r][c]:
            c += 1

    return False

# 1,  4,  7,  11
# 2,  5, *8,  12
#*3, *6, *9,  16
#*10, 13, 14, 17

matrix = [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]] 
for target in [5, 16, 99]:
    print(search2D(matrix, target))

