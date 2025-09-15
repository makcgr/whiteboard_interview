var arr = new[] { 5, 6, 7, 1, 2, 3, 4 };
Console.WriteLine(FindMinimum(arr));

//Console.WriteLine(FindMinimum([ 1, 2, 3, 4, 5 ]));
//Console.WriteLine(FindMinimum([ 1, 2 ]));
//Console.WriteLine(FindMinimum([ 2, 1 ]));

/*
Ex:
5 6 7 1 2 3 4
^           ^
l           r

Solution:
Since array is sorted, we can use the division by two strategy
    Array consists of two parts (sorted and not sorted)
        where not sorted can be 0 length if array is not rotated e.g. { 1 2 3 }

We start with left l (i=0) and right r (i=n-1) ptrs
In a while loop (l < r)
    First we check, if left is lower than right (if yes, then left is min => return left)
    Then we divide by two the right ptr to find mid (integer division)
        With each division, we check which part is sorted by comparing mid and left / right
            * We know that at this point left is higher then right
                - if mid is equal to right, then it's min => return right
                - if mid is higher than right as well:
                    there is no point in searching the lowest in the "left" part
                    since both left and mid > right and because of contingency of sort,
                    we know whole left part is sorted and has higher values
                    we will find the lowest in the right part => update left to mid+1
                - if mid is lower than right:
                    then the left part looks promising
                    we will find min in the left part => update right to mid (mid can possibly be min!)
    Return l after loop (though we should not get here since we treat = case early)
*/

static int FindMinimum(int[] arr)
{
    // Assume corner cases null/0/1 elements handled
    int l = 0, r = arr.Length - 1;

    while (l < r)
    {
        if (arr[l] < arr[r])
            return arr[l];
        var mid = l + (r - l) / 2;
        if (arr[mid] == arr[r])
            return arr[r];
        else if (arr[mid] > arr[r])
            l = mid + 1;
        else if (arr[mid] < arr[r])
            r = mid;
    }
    return arr[l];
}
