# You 2 integers n and m representing an n by m grid, determine the number of ways you can get from the top-left to the bottom-right of the matrix y going only right or down.

#Example:
#n = 2, m = 2

#This should return 2, since the only possible routes are:
#Right, down
#Down, right.


# Recall that this problem is very similar to the classic staircase problem, and has many repeated computations. This is a great use case for dynamic programming. We will use an N by M grid and index i, j will represent the number of ways we can get to that index from the top left. We will iteratively fill up this matrix using the recurrence relationship, and then return the bottom-right value at the end.


def num_ways(n, m):
  A = [[0 for _ in range(m)] for _ in range(n)]
  for i in range(n):
    A[i][0] = 1
  for j in range(m):
    A[0][j] = 1
  for i in range(1, n):
    for j in range(1, m):
      A[i][j] = A[i - 1][j] + A[i][j - 1]
  return A[-1][-1]

print (num_ways(3, 3))
# ?

