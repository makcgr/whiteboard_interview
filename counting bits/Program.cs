/* 

Counting bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

*/

var n = 8;
var result = Solution.CountBitsForEach(n, Solution.CountBitsInNumberNaive);
Console.WriteLine($"N={n}. Counted bits (naive): {string.Join(",", result)}");

result = Solution.CountBitsForEach(n, Solution.CountBitsInNumberPro);
Console.WriteLine($"N={n}. Counted bits (pro): {string.Join(",", result)}");

public class Solution
{
    public static int[] CountBitsForEach(int n, Func<int,int> countBitsFunc)
    {
        int[] result = new int[n+1];
        for(int i=0; i<=n; i++)
        {
            result[i] = Solution.CountBitsInNumberNaive(i);
        }

        return result;
    }

    /* 
    Naive solution: O(N*logN) time complexity with unnecessary operations like Log2() and Pow()
    
    To count bits, we need to figure out the powers of 2 which together will make up the number.
    
    We will represent the number as an array of a Log2(number)+1 length with 0 or 1 in the certain registers,
    corresponding to the power of 2 that make up the number.
    
    We will start with the base 2 logarithm (log2) of the given number.
    Then we will fill the array[log2] cell with the 1 and subtract the 2^(base 2 log) out of the number

    */
    public static int CountBitsInNumberNaive(int number)
    {
        if (number == 0) return 0;

        int bitDepth = (int) Math.Log2(number) + 1;

        int[] arr = new int[bitDepth];
        Array.Fill(arr, 0);

        int curr = number;
        int bitsCount = 0;

        while (curr != 0)
        {   
            var log2 = (int) Math.Log2(curr);            

            curr -= (int)Math.Pow(2, log2);
            arr[log2] = 1;
            bitsCount++;
        }

        return bitsCount;
    }

    /*
    Pro solution: O(N*logN) time complexity (all numbers * time to iterate all bits)
    Will use bitwise operators to do the shift to the right and check the least significant bit (LSB).
    */

    public static int CountBitsInNumberPro(int number)
    {
        int curr = number;
        int bitsCount = 0;
        while(curr!=0)
        {
            bitsCount += curr & 1;
            curr = curr >> 1;
        }
        return bitsCount;
    }
}