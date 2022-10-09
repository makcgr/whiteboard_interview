/*

Solution:

The idea is to iterate through array of numbers, swapping the current "val" element with the last "non-val" element
from the end of an array. We will update the current length of the array as we swap elements.
Hence we will use two pointers, i for current element, and j for exchange element.

If there are no more "non-val" elements to the right, then the algorithm has finished and we return i as new length of array.

The time complexity will be O(N), since the iterations direction is towards each other and these pointers will meet at some point.

*/

var testArr = new (int, int[])[] 
{
    (3, new []{3,3}),
    (3, new []{3,2,2,3}),
    (2, new []{0,1,2,2,3,0,4,2}),
};

var solution = new Solution();
foreach(var t in testArr)
{
    var val = t.Item1;
    var arr = t.Item2;

    Console.WriteLine($" input={val} {Print(arr)}");
    var res = (solution.RemoveElement(arr, val));
    Console.WriteLine($"result={res} {Print(arr)}");
}

static string Print(int[] arr)
{
    return $"[{string.Join(",", arr)}]";
}

public class Solution {
    public int RemoveElement(int[] nums, int val) {
        
        int len = nums.Length;       
        
        for (int i=0; i < len; i++)
        {
            bool isVal = nums[i]==val;
            
            if(isVal)
            {
                int lastNonValIx = -1;
                for (int j=len-1; j>i; j--)
                {
                    if(nums[j]!=val)
                    {
                        lastNonValIx = j;
                        break;
                    }
                }
                
                if(lastNonValIx != -1)
                {
                    nums[i] = nums[lastNonValIx];
                    nums[lastNonValIx] = val;
                    len = lastNonValIx;
                }
                else
                {
                    return i;
                }
            }            
        }
        return len;
    }
}