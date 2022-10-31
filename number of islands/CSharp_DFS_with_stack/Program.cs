
/*
Number of Islands (Leetcode)

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

1 1 0 0 0 
1 1 0 0 0 
0 0 1 0 0 
0 0 0 1 1

ex. 1. Number of islands: 3

1 0 1 1 1 
1 0 1 0 1 
1 0 1 0 1 
1 1 1 0 1

ex. 2. Number of islands: 1

Solution

Matrix of ones and zeroes can be viewed as a graph,
where each node (cell) is connected with one to four other nodes (cells). 
That is, to the right, downwards, to the left, and upwards.

We will iterate over matrix, looking for a "piece of land".

When a land is found, we will "explore" the island by looking for adjacent land pieces with DFS (depth-first-search).

DFS means, that we will put every adjacent piece of land to the stack.
We will then pop each piece from stack for processing, and eventually, we will visit them all.
To mind visited indices, we will put coordinate tuples of (x, y) into a "visited" dictionary.

So, when we found an "unvisited" island:
    We will use four "directions" for traversing it and a stack to store found pieces of land. 
    We will traverse adjacent cells in search for next "land piece".
    Each such adjacent "land piece" we will put in a stack.
    We will process items in the stack until it's empty.
    Then we will increase the number of islands.

The time complexity will be O(N) since we iterate over each cell in matrix and track visited nodes in dictionary when processing.
The space complexity will be also O(N).
*/

using System.Diagnostics;

Tests.Test1();
Tests.Test2();

public static class Tests
{
    public static void Test1()
    {
        Console.WriteLine(nameof(Test1));
        var sol = new Solution();

        char [][] a = {
            new char[] {'1', '1', '0', '0', '0'} ,
            new char[] {'1', '1', '0', '0', '0'} ,
            new char[] {'0', '0', '1', '0', '0'} ,
            new char[] {'0', '0', '0', '1', '1'}
        };

        char res = sol.NumIslands(a);
        Debug.Assert(res==3);
        Console.WriteLine($"Number of islands: {(int)res}");
    }

    public static void Test2()
    {
        Console.WriteLine(nameof(Test2));
        var sol = new Solution();

        char [][] a = {
            new char[] {'1', '0', '1', '1', '1'} ,
            new char[] {'1', '0', '1', '0', '1'} ,
            new char[] {'1', '1', '1', '0', '1'} 
        };

        char res = sol.NumIslands(a);
        Debug.Assert(res==1);
        Console.WriteLine($"Number of islands: {(int)res}");
    }
}


public class Solution {
    public char NumIslands(char[][] grid) {

        Debug.Assert(grid != null);        

        int height = grid.Length;
        int width = grid[0].Length;

        Debug.Assert(height>0 && width>0);

        var visited = new Dictionary<Tuple<int,int>, bool>();
        // directions: to the right, downwards, to the left, upwards
        var directions = new [] { Tuple.Create(1,0), Tuple.Create(0,1), Tuple.Create(-1,0), Tuple.Create(0,-1) };

        int islandsCount = 0;
        for (int x=0; x<width; x++)
        {
            for (int y=0; y<height; y++)
            {
                var curr = Tuple.Create(x,y); // current cell (node), starting from (0, 0)
                if (visited.ContainsKey(curr))
                    continue;
                
                // Searching for an "island" piece (a root node), so only unvisited 1s are relevant
                if (grid[y][x] == '1')
                {
                    // Diving into sub-algorithm exploring the island
                    var stack = new Stack<Tuple<int,int>>();
                    stack.Push(curr);

                    while(stack.Count > 0)
                    {
                        curr = stack.Pop();                            
                        if (!visited.ContainsKey(curr))
                            visited.Add(curr, true);                        
                        
                        // look for adjacent land cells to the right, downwards, to the left and upwards
                        foreach(var dir in directions)
                        {
                            int ax = (curr.Item1 + dir.Item1); // adjacent x
                            int ay = (curr.Item2 + dir.Item2); // adjacent y

                            // adjacent cell coords should be within matrix
                            if(0 <= ax && ax < width && 0 <= ay && ay < height && grid[ay][ax] == '1')
                            {
                                var next = Tuple.Create(ax, ay);
                                if (!visited.ContainsKey(next))                            
                                    stack.Push(next);
                            }
                        }                        
                    }
                    // island is traversed
                    islandsCount++;                        
                }
            }
        }
 
        return (char)islandsCount;
    }
}