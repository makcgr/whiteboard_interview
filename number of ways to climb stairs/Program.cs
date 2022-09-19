/*

Number of Ways to Climb Stairs

You are given a positive integer N which represents the number of steps in a staircase. 
You can either climb 1 or 2 steps at a time. 
Write a function that returns the number of unique ways to climb the stairs.
*/

var sol = new Solution();
var result= sol.ClimbStairs1(5);
Console.WriteLine($"Solution 1, recursive: O(2^N) result = {result}");

result = sol.ClimbStairs2(5);
Console.WriteLine($"Solution 2, dynamic: O(N) result = {result}");

public class Solution
{
    // Solution 1
    // Time complexity: O(2^N) since for each step N, we have two choices
    // to reach it (either 1 or 2 steps). The total number of permutations
    // is 2 * 2 * 2 * 2 * ..., so the time complexity is logarithmic.

    public int ClimbStairs1(int n)
    {
        return Fib(n+1);
    }

    public int Fib(int n)    
    {
        if (n<=1) return n;

        return Fib(n-1) + Fib(n-2);
    }


    /*
     Solution 2
     Here we do computations iteratively
     from the bottom up.
     Let's visualize the step ladder e.g. for n=5 with 5 steps:

             _  0
           _| 0
         _| 0
       _| 0
     _| 1
    | 1

    Each step we will map to a cell in the array.
    Initial values in the array of N+1 cells will be:

    [1][1][0][0][0][0]

    NOTE: there is extra (N+1)th cell to store the overall number of ways.

    For first two steps, n of ways to climb there is 1.
    Now for third step, we can climb there with sum of ways for two previous steps.
    We continue like this for the rest of ladder (array) until we reach the top (array[n]):
    ways(step[N]) = ways(step[N-1]) + ways(step[N-2])

    Time complexity: O(N), since this is a single pass.
    */
    public int ClimbStairs2(int n)
    {
        int[] arr = new int[n+1];
        Array.Fill(arr, 0);

        arr[0] = 1;
        arr[1] = 1;

        for (int i=2; i <= n; i++)
        {
            int j = 1;
            while (j <= 2 && j <=i)
            {
                arr[i] = arr[i] + arr[i-j];
                j = j + 1;
            }
        }
        return arr[n];
    }
}