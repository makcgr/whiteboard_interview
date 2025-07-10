// Two Sum
//Find indices of two numbers in an array that add up to a specific target.

// Returns (-1, -1) if not found
(int, int) FindTwoIndices(int[] arr, int addUpTo)
{
    // TODO Implement

    // Check corner case

    // Iterate over array (point the first number in pair)
    // Iterate over array the second time (point the second number in pair)
    // Check sum, and if the sum of two matches, return result
    // Return (-1, -1)
    // Complexity: O(N^2) since we iterate twice
    // To improve: convert an array to hash table

    if (arr == null || arr.Length < 2)
        throw new ArgumentException(nameof(arr));

    // first variant (naive)
    
	for (int i=0; i<arr.Length; i++)
	{
		for (int j=i+1; j<arr.Length; j++)
		{
			if (addUpTo == (arr[i] + arr[j]))
				return (i, j);
		}
	}   

    // enhanced variant (no second iteration)
    /*
    var dict = new Dictionary<int, int>();
    for (int i = 0; i < arr.Length; i++)
    {
        if (i > 0)
        {
            if (dict.ContainsKey(addUpTo - arr[i]))
                return (dict[addUpTo - arr[i]], i);
        }
        dict[arr[i]] = i;
    }
    */

    return (-1, -1);
}

var arr = new int[] { 1, 5, 7, 3, 6, 14, 22, 4, 4 };
// Let's find sum of 8
var (i1, i2) = FindTwoIndices(arr, 8);
Console.WriteLine($"First: {i1} ({arr[i1]}), second: {i2} ({arr[i2]})");