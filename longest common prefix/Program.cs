var arr = new [] { "flower", "flow", "flight" };
Console.WriteLine(LongestCommonPrefix(arr));

static string LongestCommonPrefix(string[] arr) {
	if (arr == null || arr.Length == 0) return string.Empty;
	if(arr.Length==1) return arr[0];

	int currentLen = 0;
	for (int i=0; i<arr[0].Length; i++) {
		for (int j=0; j<arr.Length; j++) {
			if (arr[j].Length < (i+1) || arr[j][i] != arr[0][i])
			{
				return arr[0].Substring(0,currentLen);
			}
		}
		currentLen++;
	}
	return arr[0].Substring(0,currentLen);
} 
