using System;
using System.Collections.Generic;

int[][] testArrays = new int[][]
{
    new int[] {2, 4, 5, 3, 3, 9, 2, 2, 2},
    new int[] {1, 1, 1, 1},
    new int[] {1, 1, 1, 1, 1, 1, 2},
};

foreach(var arr in testArrays)
{
    Console.Write("Array: ");
    foreach(var x in arr) Console.Write("{0} ",x);
    Console.WriteLine();
    Console.WriteLine("Answer: {0}", CanSplitIntoThreeEqualParts(arr));
}

// Time complexity: O(N)
// Space complexity: O(N)
static bool CanSplitIntoThreeEqualParts(int[] array)
{
    if(array==null || array.Length<5)
        return false;

    int i=1, j=array.Length-2;
    int sumLeft = 0, sumMiddle = 0, sumRight = 0;
    int total_sum = 0;
    Array.ForEach(array, x => total_sum+=x);

    sumLeft += array[i-1];
    sumRight += array[j+1];

    while((i+1)<j)
    {
        if(sumLeft < sumRight)
        {
            sumLeft += array[i];
            i++;
        }
        else if (sumRight < sumLeft)
        {
            sumRight += array[j];
            j--;
        }
        else
        {
            sumMiddle = total_sum - sumLeft - sumRight - array[i] - array[j];
            if (sumMiddle < sumLeft)
                return false;
            else if (sumMiddle > sumLeft)
            {
                sumLeft += array[i]; i++;
                sumRight += array[j]; j--;
            }
            else
                return true;
        }
    }
    return false;
}