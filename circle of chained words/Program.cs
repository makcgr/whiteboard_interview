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

- can start from any word in the list, each word is a chance to build a full circle
- if any word does not have any other suitable next word from the list, there is no chance to build a circle 
- "the circle" is an array of words 
    - where each word's last char is the same as next word's first char, except for last word in the array
- once the circle is built, the number of words used in chain equals total number of word, 
  and the last word's last char matches the first word's first char), we can finish our program

- regarding storage:
  we need to store word's indices in order ("circle builder array" of N integers)

- algo
    - will have 
    - must have "current word" pointer
    - must have "potentially suitable word" pointer
    - must have "used words" list (or dictionary)
    - must have "circle builder" list where suitable words are placed subsequently maintaining chained order

    - will start with the first word in list
    - when "suitable" next word is found, it can be marked as "used" and placed into "circle builder" list 
    - "suitable" words must be looked starting from the beginning of word list, excluding "current word" and "used" words,
        until there are no more words available
         - if a word is "suitable": 
                * it is added to "used words" list/dict, 
                * it is added to "circle builder array", 
                * the "current word" pointer is increased until the next unused word or until there are no unused words left
         - if a word is not "suitable": 
                increase "potential suitable word" pointer
    
    - if there is no suitable word found, then the "words circle" is not possible

    - processing is over when the length of "the circle builder" is equal to the length of list
        - check the "circle builder array": 
          the last word's last char should be the same as the first word's first char. 
          if it's true, the "words circle" is built, otherwise it's not possible. 
 
- optimizations
    - can store "used words" in a hashtable (Dictionary) 
        * e.g. word is a key in Dictionary<string,bool>, and value means if it is "used" in circle
        * or index of word is a key in Dictionary<int, bool>, and value means if it is "used" in circle
        * this will give us O(1) lookup time for each word 

    - instead of traversing all the words in a list to find a "suitable", can store "potentially suitable" words 
        in a separate list, deleting used ones,  so the number of checks will be decreased - performance gain 

    - can use indices instead of strings for "used words dictionary", "circle builder", it will also allow duplicate words 

- Time complexity: 
    if words starting letters are unique: O(N) since there is actually a limited number of edges for each word (every word can have only one edge)
    if there can be several words with the same starting letter (for iterative algorithm): O(N^2)

  Can improve time by introducing extra list for "not used words" 
*/

var testCases = new []
{
    new [] {"eggs", "karat", "apple", "snack", "tuna"},                     // correct: true
    //new [] {"eggs", "karat", "apple", "snack", "tuna", "sage", "ears"},     // correct: true (will fail for recursive variant, since a dictionary with first letters is used)
    new [] {"axb", "bxc", "cxd", "dxa"},                                    // correct: true
    new [] {"bxc", "axb", "dxa", "cxd"},                                    // correct: true
    new [] {"cxd", "axb", "bxc", "dxa"},                                    // correct: true
    //new [] {"aba", "aca"},                                                  // correct: true  (will fail for recursive variant, since a dictionary with first letters is used)
    new [] {"eggs", "karat", "snack", "tulip", "parcel"},                   // correct: false
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
    Console.Write($"\tResult (iterative): {CanChainWords(testWords)}\t");
    Console.WriteLine($"Result (recursive): {CanChainWordsRecursive(testWords)}");
    
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

bool CanChainWordsRecursive(string[] words)
{
    if (words == null || words.Length < 2)
    {
        return false;
    }

    var graph = new Dictionary<char, List<string>>();
    foreach(var word in words)
    {
        graph.Add(word[0], new List<string>() { word });
    }
    var result = false;
    var visited = new Dictionary<string, bool>();
    foreach(var word in words)
    {
        visited.Add(word, false);
    }
    result = DepthFirstSearch(graph, visited, words[0], words[0], words.Length);

    return result;
}

bool DepthFirstSearch(Dictionary<char, List<string>> graph, Dictionary<string, bool> visited, string current, string startWord, int length)
{
    if (length == 1)
    {
        return startWord[0] == current[^1];
    }

    visited[current] = true;
    foreach (var neighbor in graph[current[^1]])
    {
        if (!visited[neighbor])
        {
            return DepthFirstSearch(graph, visited, neighbor, startWord, length-1);
        }
    }
    // no unvisited "neighbor", thus no sense to mark as visited. Visited marks should belong only to all words in "chain"
    visited[current] = false;
    return false;
}