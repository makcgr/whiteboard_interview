#
#
#
#

from typing import List

def search2D(matrix: List[List[int]], val: int):
    rowsNum = len(matrix)
    columnsNum = len(matrix[0])

    l, r = 0, rowsNum * columnsNum - 1
    while l <= r:
        mid = l + (r - l) // 2
        row, col = divmod(mid, columnsNum)
        midVal = matrix[row][col]
        if midVal == val:
            return True
        elif midVal < val:
            l = mid + 1
        elif midVal > val:
            r = mid - 1
    return False

# 1,  3,  5,  7
# 10, 11, 18, 20
# 23, 30, 31, 35

matrix = [[1,3,5,7],[10,11,18,20],[23,30,31,35]] 
for target in [5, 18, 99]:
    print(search2D(matrix, target)) 
