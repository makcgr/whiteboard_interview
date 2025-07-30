/* 
Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
*/

int[] nums = [1, 2, 3, 4];
Console.WriteLine(string.Join(", ", new Solution().ProductExceptSelf(nums)));

public class Solution
{
    public int[] ProductExceptSelf(int[] nums)
    {

        /* 
        iterate through array
            first pass: left to right, multiply items except current index
            second pass: right to left, multiply items except current index 
        */
        var n = nums.Length;

        int[] res = new int[n];
        res[0] = 1;

        // Compute left products (excluding self)
        for (int i = 1; i < n; i++)
        {
            res[i] = res[i - 1] * nums[i - 1];
        }

        // Compute right product (excluding self) and multiply to left product
        var right = 1;
        for (int i = n - 1; i >= 0; i--)
        {
            res[i] = res[i] * right;
            right *= nums[i];
        }

        return res;
    }
}