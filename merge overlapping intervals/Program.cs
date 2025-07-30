var intervals = new int[][] { [1,3], [2,6], [8,10], [15,18] };
var result = Merge(intervals); // [[1,6],[8,10],[15,18]]
foreach (var arr in result)
{
    Console.Write($"[{string.Join(", ", arr)}]");
    if (arr == result.Last()) Console.WriteLine();
}

int[][] Merge(int[][] intervals)
{
    if (intervals.Length == 0)
        return [];

    Array.Sort(intervals, (a, b) => a[0].CompareTo(b[0]));

    var merged = new List<int[]>();
    int[] current = intervals[0];

    foreach (var interval in intervals)
    {
        if (interval[0] <= current[1])
            current[1] = Math.Max(current[1], interval[1]);
        else
        {
            merged.Add(current);
            current = interval;
        }
    }
    merged.Add(current);

    return merged.ToArray();
}
