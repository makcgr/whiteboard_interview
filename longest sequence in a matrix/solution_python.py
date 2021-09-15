# Given a grid, find a maximum number of connected colors:

# 0, 0, 1, 2
# 0, 1, 2, 1
# 2, 1, 1, 1

from collections import deque 

def GetColor(grid, coordinates):
    return grid[coordinates[1]][coordinates[0]]

def IsValidCoord(coord, grid):
    return (coord[0] >= 0) \
        and (coord[0]<len(grid[0])) \
        and (coord[1] >= 0) \
        and (coord[1]<len(grid))

DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]
def CountLongestSequence(grid, coordinates, tb_visited):
    length = 1
    color = GetColor(grid, coordinates)
    queue = deque([coordinates])
    tb_visited[coordinates] = True
    while (len(queue)>0):
        cur_coord = queue.popleft()
        for direction in DIRECTIONS:
            adjacent_coord = (cur_coord[0]+direction[0], cur_coord[1]+direction[1])
            if IsValidCoord(adjacent_coord, grid) \
                and not adjacent_coord in tb_visited \
                and color == GetColor(grid, adjacent_coord):
                queue.append(adjacent_coord)
                tb_visited[adjacent_coord] = True
                length += 1

    return length

def FindLongestSequence(grid):
    longest_len = -1
    tb_visited = {}
    for y, row in enumerate(grid):
        for x, item in enumerate(row):
            coordinates = (x,y)
            #print("%d, %d: %s" % (x, y, item))
            if (coordinates in tb_visited):
                continue
            counted_len = CountLongestSequence(grid, coordinates, tb_visited)
            if counted_len > longest_len:
                longest_len = counted_len

    return longest_len

grid = [[0, 0, 1, 2], [0, 1, 2, 1], [2, 1, 1, 1]]

print(FindLongestSequence(grid))

# Time complexity is O(N) and space complexity is O(N) also.