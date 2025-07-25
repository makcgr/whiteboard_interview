var arr = new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
Console.WriteLine(string.Join(", ", arr));
Console.WriteLine(string.Join(", ", RotateArray(arr, 3)));

static int[] RotateArray(int[] arr, int k)
{
    if (arr == null || arr.Length == 0) return arr;

    var rotated = new int[arr.Length];

    int steps = arr.Length;
    int curr = 0;
    int offset = (k % arr.Length);

    for (int i = 0; i < arr.Length; i++)
    {
        if ((i + offset) < arr.Length)
            rotated[i + offset] = arr[i];
        else
            rotated[i + offset - arr.Length] = arr[i];
    }
    return rotated;
}