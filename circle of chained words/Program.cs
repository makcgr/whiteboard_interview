/*
Two words can be 'chained' if the last character of the first word is the same as the first character of the second word.

Given a list of words, determine if there is a way to 'chain' all the words in a circle.

Example:
Input: ['eggs', 'karat', 'apple', 'snack', 'tuna']
Output: True
Explanation:
The words in the order of ['apple', 'eggs', 'snack', 'karat', 'tuna'] creates a circle of chained words.
*/


/*

Solution

- can start from any word in the list
- each word is a chance to build a circle
- if any word does not have any suitable next word from the list, there is no chance to build a circle 
- "the circle" is an array of words 
   - where each word's last char is the same as next word's first char, except for last word in the array
- once the circle is built, the number of words used in chain equals total number of word, 
  and the last word's last char matches the first word's first char), we can finish our program

- regarding storage:
  - we need to store word's indices in order ("circle builder array" of N integers)

- algo:
  - must have "current word" pointer
  - must have "potentially suitable word" pointer
  - each word can be marked as "used" (e.g. word is a key in Dictionary<string,bool>, and value can be "used" boolean value),
    this will give us O(1) access time to each word
  - "suitable" words must be looked starting from the beginning of Dictionary, excluding "current word" and "used" words,
    until there are no such words available (reached the end of Dictionary)
     - if a word is "suitable": 
        * it is marked as "used" in the dictionary, 
        * it's index is added to "circle builder array", 
        * the "current word" pointer is increased until the next unused word or until there are no unused words left
     - if a word is not "suitable":
        increase "potential suitable word" pointer
  - if length of "the circle" is equal to the length of list, check the "circle builder array": 
    the last word's last char should be the same as the first word's first char - circle is built, otherwise it's not possible. 

*/

//var words = new [] {"eggs", "karat", "apple", "snack", "tuna"};
//// The circle can be built: { "apple", "eggs", "snack", "karat", "tuna" }

var testCases = new []
{
    new [] {"eggs", "karat", "apple", "snack", "tuna"},                     // correct: true
    new [] {"eggs", "karat", "apple", "snack", "tuna", "sage", "ears"},     // correct: true
    new [] {"axb", "bxc", "cxd", "dxa"},                                    // correct: true
    new [] {"bxc", "axb", "dxa", "cxd"},                                    // correct: true
    new [] {"cxd", "axb", "bxc", "dxa"},                                    // correct: true
    new [] {"aba", "aca"},                                                  // correct: true
    new [] {"eggs", "karat", "strawberries", "snack", "tulips"},            // correct: false
    new [] {"axb", "bxc", "cxd", "dxe"},                                    // correct: false
    new [] {"aba"},                                                         // correct: false
    new string[] {},                                                        // correct: false
};

foreach (var testWords in testCases)
{
    foreach(var word in testWords)
    {
        Console.Write("{0}{1}",word, word==testWords[testWords.Length-1]?". ":", ");
    }
    Console.WriteLine($"Result: {CanChainWords(testWords)}");
}

bool CanChainWords(string[] words)
{
        if (words == null || words.Length < 2)
        {
                // Should have more than one word in words list parameter
                return false;
        }

        var usedDictionary = new Dictionary<string, bool>(words.Length);
        var circleBuilder = new List<string>();

        // Init the "Used words" dictionary with "false" to have O(1) for lookup
        for(int i=0; i<words.Length; i++)
        {
            usedDictionary.Add(words[i], false);
        }
 
        // Start the
        circleBuilder.Add(words[0]);
        usedDictionary[words[0]] = true;

        var currentIx = 0;
        while (circleBuilder.Count < words.Length) // if circle builder's length is equal to words count, no need to find the suitable "next" (circle is built!)
        {
            var current = words[currentIx];

            // try to find suitable "next" word by traversing the dictionary and also checking "used" flag
            bool found = false;

            for(int potentiallySuitableIx=0; potentiallySuitableIx < words.Length; potentiallySuitableIx++)
            {
                    var potentiallySuitable = words[potentiallySuitableIx];
                    bool used = usedDictionary[potentiallySuitable];

                    if (!used && current[current.Length-1]==potentiallySuitable[0])
                    {
                            found = true;
                            usedDictionary[potentiallySuitable] = true;
                            circleBuilder.Add(potentiallySuitable);
                            currentIx = potentiallySuitableIx;

                            break;
                    }
            }
            if (!found)
            {
                    return false;
            }
        }
        var lastWord = circleBuilder[circleBuilder.Count-1];
        var firstWord = circleBuilder[0];
        return lastWord[lastWord.Length-1] == firstWord[0];
}
