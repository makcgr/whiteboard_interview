using System.Diagnostics;

char [][] a = {
    new char[] {'1', '1', '0', '0', '0'} ,
    new char[] {'1', '1', '0', '0', '0'} ,
    new char[] {'0', '0', '1', '0', '0'} ,
    new char[] {'0', '0', '0', '1', '1'}
};

char res = new Solution().NumIslands(a);
Debug.Assert(res==3);
Console.WriteLine($"Number of islands: {(int)res}");


public class Solution 
{
    public bool InRange(char[][] grid, int row, int col)
    {
        int height = grid.Length; 
        int width = grid[0].Length;
        return 0 <= row && row < width && 0 <= col && col < height;
    }

    public char NumIslands(char[][] grid) {
        int height = grid.Length; 
        int width = grid[0].Length;
        int count = 0;
        for (int x=0; x<width; x++)
            for (int y=0; y<grid.Length; y++)
            {
                if(grid[y][x]=='1')
                {
                    count++;
                    DFSRecursive(grid, x, y);
                }
            }
        return (char)count;
    }

    public struct Coord { 
        public int X; public int Y; 
        public Coord(int X, int Y) { this.X = X; this.Y = Y; }
    };

    Coord[] directions = new [] { new Coord(1,0), new Coord(0, -1), new Coord(-1, 0), new Coord(0, 1)};
    public void DFSRecursive(char[][] grid, int x, int y)
    {
        grid[y][x] = '2';
        foreach(var dir in directions)
        {
            var nx = x+dir.X; var ny = y+dir.Y;
            if (InRange(grid, nx, ny) && grid[ny][nx]=='1')
            {
                DFSRecursive(grid,nx,ny);
            }
        }
    }
}