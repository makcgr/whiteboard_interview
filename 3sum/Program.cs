

IList<IList<int>> ThreeSum(int[] nums) 
{
    if (nums==null || nums.Length<3) throw new ArgumentException(nameof(nums));

    var result = new List<IList<int>>();
    var htResults = new HashSet<Tuple<int,int,int>>();

    // Existing numbers between nums[i] and nums[j]
    for(int i=0; i<nums.Length-2; i++)
    {
        int target = 0 - nums[i];
        var htExistingNumbers = new HashSet<int>();
        
        for(int j=i+1; j<nums.Length; j++)
        {
            if(htExistingNumbers.Contains(target-nums[j]))
            {
                var array = new[]{nums[i], target-nums[j], nums[j]};
                Array.Sort(array);
                var resultTuple = new Tuple<int, int, int>(array[0], array[1], array[2]);
                if (!htResults.Contains(resultTuple))
                {
                    htResults.Add(resultTuple);
                    result.Add(array);
                }
            }
            else
            {
                htExistingNumbers.Add(nums[j]);
            }
        }
    }
    return result;    
}


int [] nums = new[] {-1,0,1,2,-1,-4};

var result = ThreeSum(nums);

foreach(var arr in result)
{
    Console.Write($"{arr[0]} {arr[1]} {arr[2]}\n");
}

