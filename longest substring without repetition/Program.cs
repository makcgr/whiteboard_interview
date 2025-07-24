var str = "abrkaabcdefghijjxxx";
Console.WriteLine($"Answer: {GetLongestSubstringWORepetitions(str)}");

static int GetLongestSubstringWORepetitions(string input)
{
	if (input == null || input.Length == 0)
		return 0;

	var arr = input.ToCharArray();	
	var head = 0;
	var tail = 0;
	var maxLen = 0;
	var hashSet = new HashSet<char>();
	while (head < arr.Length) {
		if (hashSet.Contains(arr[head])) {
			maxLen = Math.Max(maxLen, head-tail);
			hashSet.Clear();
			tail = head;
		}
		hashSet.Add(arr[head]);
		head++;			
	}
	return Math.Max(maxLen, head-tail);
}