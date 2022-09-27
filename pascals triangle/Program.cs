/*
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

         1
       1   1
     1   2   1
   1   3   3   1
 1   4   6   4   1 

Example:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
 

Constraints:
1 <= numRows <= 30
*/

var res = new Solution().Generate(5);

foreach(var row in res)
{
    Console.WriteLine(string.Format("[{0}]", string.Join(",", row.ToList())));
}

public class Solution 
{
    // Solution: 
    // We build "Pascal's triangle" jagged array (array of arrays),
    // starting from the top of triangle.
    // Each next inner array is [n+1] elements when compared to the previous array of [n]
    // From 3rd row on we begin to form values of current row as the sum of above's "left" and "right" values.
    // Time complexity is O(N^2) since we iterate two times and space complexity is also O(N^2) 
    // since we build the whole triangle.
    public IList<IList<int>> Generate(int numRows) 
    {
        int[][] triangleArray = new int[numRows][];

        for (int num = 1; num <= numRows; num++)
        {
            triangleArray[num-1] = new int[num];    // we are row with index [num-1]
            var currentRow = triangleArray[num-1];
            
            for(int x=0; x<=num-1; x++)
            {                
                if(num==1 || num==2)
                {
                    currentRow[x] = 1;
                }
                else
                {
                    var aboveRow = triangleArray[num-2];  // the row above us is [num-2]

                    var left = x-1 < 0 ? 0 : aboveRow[x-1];               // number above and to the left
                    var right = x > aboveRow.Length-1 ? 0 : aboveRow[x];  // number above and to the right

                    currentRow[x] = left + right;
                }                    
            }
        }
        return triangleArray;
    }

    public IList<IList<int>> Generate2(int numRows) 
    {
        var arrayList = new List<IList<int>>();        
        var row = new int[numRows];
        Array.Fill(row, 1);
        
        foreach(var i in Enumerable.Range(0, numRows))
        {
            arrayList.Add(row[0..(i+1)].ToList());

            var last = row[0];            
            foreach(var j in Enumerable.Range(1, i))
            {
                var temp = row[j];
                row[j] = last + row[j];
                last = temp;
            }
        }
        return arrayList;
    }
}