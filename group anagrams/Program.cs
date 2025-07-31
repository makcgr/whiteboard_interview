var strs = new string[] { "eat", "tea", "tan", "ate", "nat", "bat" };

foreach (var group in GroupAnagrams(strs).ToArray())
    Console.Write("{" + string.Join(", ", group.ToArray()) + "}");
Console.WriteLine();

List<List<string>> GroupAnagrams(string[] strs)
{
    var groups = new Dictionary<string, List<string>>();
    
    foreach (string str in strs)
    {
        string key = string.Concat(str.OrderBy(c => c));
        
        if (!groups.ContainsKey(key))
            groups[key] = new List<string>();
            
        groups[key].Add(str);
    }
    
    return groups.Values.Where(list => list.Count>1).ToList();
}