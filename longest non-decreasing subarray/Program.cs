/*  
 [1, 2, 2, 3, 1, 4, 5, 6]
 => 
 [1, 4, 5, 6]
 */

public class Solution
{
    public static int LongestNonDecreasing(int[] arr)
    {
        if (arr == null || arr.Length == 0)
            return 0;

        int maxLen = 1;
        int currLen = 1;
        for (int i=1; i<arr.Length; i++)
        {
            if (arr[i]>arr[i-1])
                currLen++;
            else
            {
                currLen = 1;
                maxLen = Math.Max(maxLen, currLen);
            }
        }
        return Math.Max(maxLen, currLen);
    }

    public static void Main(string[] args)
    {
        var arr = new int[] { 1, 2, 2, 3, 1, 4, 5, 6 };
        Console.WriteLine($"{Solution.LongestNonDecreasing(arr)}");
    }
}
