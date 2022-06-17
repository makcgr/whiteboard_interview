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

var words = new [] {"eggs", "karat", "apple", "snack", "tuna"};
//{ "apple", "eggs", "snack", "karat", "tuna" }

var result = CanChainWords(words);

Console.WriteLine($"Can chain words: {result}");

bool CanChainWords(string[] words)
{
    if (words == null)
        throw new ArgumentNullException(nameof(words));
    if (words.Length < 2)
        throw new ArgumentException($"Array {nameof(words)} has insufficient words count");

    int currentWordIx = 0;

    var dictionary = new Dictionary<int, bool>(words.Length);
    var circleBuilder = new List<int>();
    
    for(int i=0; i<words.Length; i++)
    {
        dictionary.Add(i, false);
    }
 
    while (currentWordIx<words.Length) 
    {
        var currentWord = words[currentWordIx];
        if (!dictionary[currentWordIx]) //check if the word was used already in the circle builder
        {       
            circleBuilder.Add(currentWordIx);
            dictionary[currentWordIx] = true;

            if(circleBuilder.Count < words.Length) // if it's the last word, no need to find the suitable "next"
            {
                // try to find suitable "next" word by traversing the dictionary and also checking "used" flag
                int potentiallySuitableIx = 0;
                bool found = false;    
                while (!found && potentiallySuitableIx < words.Length)
                {
                    string potentiallySuitableWord = words[potentiallySuitableIx];
                    bool used = dictionary[potentiallySuitableIx];

                    if (!used && currentWord[currentWord.Length-1]==potentiallySuitableWord[0])
                    {
                        found = true;
                        dictionary[potentiallySuitableIx] = true;
                        circleBuilder.Add(potentiallySuitableIx);
                        break;
                    }
                    potentiallySuitableIx++;
                }
                if (!found)
                {
                    return false;
                }
            }
        }
        currentWordIx++;
    }
    var lastWord = words[circleBuilder[circleBuilder.Count-1]];
    var firstWord = words[circleBuilder[0]];
    return lastWord[lastWord.Length-1] == firstWord[0];
}
