
int [] nums = [-1, 0, 1, 2, -1, -4];

var res = ThreeSum(nums);
foreach(var tuple in res)
    Console.WriteLine($"({tuple.Item1}, {tuple.Item2}, {tuple.Item3})");

Console.WriteLine(string.Join(", "), res);

(int, int, int)[] ThreeSum(int[] nums) 
{
    if (nums.Length < 3) return [];
    var result = new HashSet<(int,int,int)>();

    // Existing numbers between nums[i] and nums[j]
    for(int i=0; i<nums.Length-2; i++)
    {
        int target = 0 - nums[i];
        var hashSet = new HashSet<int>();
        
        for(int j=i+1; j<nums.Length; j++)
        {
            if(hashSet.Contains(target - nums[j]))
            {
                int[] arr = [nums[i], target - nums[j], nums[j]];
                Array.Sort(arr);
                result.Add((arr[0], arr[1], arr[2]));
            }
            else
            {
                hashSet.Add(nums[j]);
            }
        }
    }
    return result.ToArray();
}

