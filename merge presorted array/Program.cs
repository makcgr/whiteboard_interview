/*
Write a function that accepts two already-sorted arrays of integers and returns an array with all elements from both that is also sorted.

E.g.
{ 1, 3, 7, 8  }
{ 1, 2, 7, 10 }

Result:
{ 1, 1, 2, 3, 7, 7, 8, 10 }

Bonus task: instead of 2 inputs, program should take any number of inputs
 */

namespace MergePresortedArray
{
    class Solution
    {
        private static int[] MergePresortedArrays(int[] arr1, int[] arr2)
        {
            int[] res = new int[arr1.Length + arr2.Length];

            int cur1 = 0;
            int cur2 = 0;
            int ix = 0;

            while(cur1 < (arr1.Length-1) || cur2 < (arr2.Length-1))
            {
                if (cur1 < (arr1.Length - 1) && cur2 < (arr2.Length - 1))
                {
                    if (arr1[cur1] < arr2[cur2])
                    {
                        res[ix++] = arr1[cur1++];
                    }
                    else
                    {
                        res[ix++] = arr2[cur2++];
                    }
                }
                else if (cur1 < (arr1.Length -1))
                {
                    res[ix++]=arr1[cur1++];
                }
                else if (cur2 < (arr2.Length -1))
                {
                    res[ix++]=arr2[cur2++];
                }
            }

            return res;
        }

        static void Main(string[] args)
        {
            int[] arr1 = { 1, 3, 7, 8  };
            int[] arr2 = { 1, 2, 7, 10 };

            int[] res = MergePresortedArrays(arr1, arr2);

            foreach (var x in res)
                Console.Write(string.Format("{0} ", x));
        }
    }
}
