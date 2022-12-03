/*
Problem:
Given a string, return the maximum length of repeating characters.

1) "" -> 0
2) "a" -> 1 
3) "abbc" -> 2
4) "adddaabaa" -> 3
5) "aaaaa" -> 5   

Solution:

We will have two pointers, one pointing to the first character and then another one pointing to the second one.
Then we will iterate over a string with one pass, each time incrementing pointers and counting repeating letters.

Each time the letter is repeated, we will increase the "current letter" counter. 
Each time the letter changes, we will reset the counter to 1.

We will track the maximum repeating characters number in the result variable, setting it to "current counter" if it's greater.
*/

string[] testCases = new [] {
    "",
    "a",
    "abbc",
    "adddaabaa",
    "aaaaa",
};

foreach(var s in testCases)
{
    var result = GetMaxSameLetterCount(s);
    Console.WriteLine($"{s}: {result}");
}

int GetMaxSameLetterCount(string s)
{
    if (s == null || s.Length == 0)
        return 0;
    
    if(s.Length == 1)
        return 1;

    int ptr = 0;
    int count = 1;
    int result = 1;
    for(int i=1; i <= s.Length-1; i++)
    {
        count = (s[ptr] == s[i] ? count+1 : 1);        
        
        if (result < count)
            result = count;

        ptr++;     
    }
    return result;
}