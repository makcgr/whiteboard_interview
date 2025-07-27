// nums = [1,3,-1,-3,5,3,6,7], k = 3
// res => [3,3,5,5,6,7]

var nums = new int[] { 1, 3, -1, -3, 5, 3, 6, 7 };
Console.WriteLine(string.Join(", ", SlidingWindowMaximum(nums, 3)));

static int[] SlidingWindowMaximum(int[] nums, int k)
{
    if (nums.Length * k == 0)
        return [];

    int[] res = new int[nums.Length - k];
    LinkedList<int> deque = new();
    var resIx = 0;
    for (int i = 0; i < nums.Length - 1; i++)
    {
        if (i > k - 1 && deque.Count > 0 && deque.First() < i)
            deque.RemoveFirst();    // remove index not relevant to window 

        while (deque.Count > 0 && nums[deque.Last()] <= nums[i])    // remove not maximal elements from relevant to window 
            deque.RemoveLast();

        deque.AddLast(i);     // now indexes are sorted by value of elements (DESC)

        if (i >= k - 1)
            res[resIx++] = nums[deque.First()];
    }
    return res;
}

/*
1, 3, -1, -3, 5, 3, 6, 7
k=3
1, 3, -1
   3, -1, -3
      -1, -3, 5
          -3, 5, 3
                 3, 6, 7
deque   1
i       0
*/