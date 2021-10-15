using System;
using System.Collections.Generic;

TestArrayToBST();

static void TestArrayToBST()
{
    int[][] arrays = new int[][]
    {
        new int[] {},
        new int[] {1},
        new int[] {1,2},
        new int[] {1,2,3},
        new int[] {1,2,3,4},
        new int[] {-10, -3, 0, 5, 9},
        new int[] {-10, -3, -1, 0, 5, 7, 9}
    };

    foreach(var arr in arrays)
    {
        Console.WriteLine("Array: ");
        foreach(var x in arr)
            Console.Write("{0} ",x);
        Console.WriteLine();

        Console.WriteLine("Sorted iteratively in a linear way: {0}", SortedArrayToBST(arr));

        Console.WriteLine("Sorted iteratively with stack: {0}", SortedArrayToBSTIterativeWithStack(arr));

        Console.WriteLine("Sorted recursively: {0}", SortedArrayToBSTRecursive(arr));
    }
}

// Time complexity:  O(N)
// Space complexity: O(N)
static Node SortedArrayToBST(IList<int> array)
{
    if (array == null || array.Count==0) return null;

    if (array.Count == 1)
        return new Node(array[0]);

    int rootIx = array.Count / 2;

    Node rootNode = new Node(array[rootIx]);
    Node node = rootNode;
    for (int i = rootIx+1; i<array.Count; i++)
    {
        node.Right = new Node(array[i]);
        node = node.Right;
    }
    node = rootNode;
    for (int i =rootIx-1; i >= 0; i--)
    {
        node.Left = new Node(array[i]);
        node = node.Left;
    }

    return rootNode;
}

// TC: for each element, be a node created, so O(N)
// SC: There would be new arrays allocation.
// Since we are creating BST then SC would be O(logN)
static Node SortedArrayToBSTRecursive(int[] array)
{
    if (array.Length == 0)
        return null;
    else if (array.Length == 1)
        return new Node(array[0]);
    else // array.Count > 1
    {
        int halfLength = array.Length/2;
        int midIndex = halfLength;
        
        var node = new Node(array[midIndex]);

        var leftSubArray = new int[halfLength];
        Array.Copy(array,0,leftSubArray,0,halfLength);
        node.Left = SortedArrayToBSTRecursive(leftSubArray);

        if((midIndex+1)!=array.Length)
        {
            int rightSubArrayLen = halfLength - (array.Length % 2 == 0 ? 1 : 0);
            var rightSubArray = new int[rightSubArrayLen];
            Array.Copy(array,midIndex+1,rightSubArray,0,rightSubArrayLen);
            node.Right = SortedArrayToBSTRecursive(rightSubArray);
        }
        return node;
    }
}

// TC: O(N)
// SC: O(logN)
static Node SortedArrayToBSTIterativeWithStack(int[] array)
{
    if (array==null || array.Length==0)
        return null;

    if (array.Length==1)
        return new Node(array[0]);

    
    var stack = new Stack<Tuple<int[],Node>>();

    var node = new Node(0);
    stack.Push(new Tuple<int[],Node>(array, node));

    while(stack.Count > 0)
    {
        var tuple = stack.Pop();
        int[] arrIn = tuple.Item1;
        Node nodeIn = tuple.Item2; 
        if (arrIn.Length==0) throw new InvalidOperationException();
        if (arrIn.Length==1)
        {
            nodeIn.Value = arrIn[0];
        }
        else // arrIn.Length > 1
        {
            int halfLength = arrIn.Length / 2;
            int midIndex = halfLength;
            
            nodeIn.Value = arrIn[midIndex];

            var leftNode = new Node(0);
            nodeIn.Left = leftNode;
            stack.Push(new Tuple<int[], Node>(arrIn[..midIndex], leftNode));

            if ((midIndex+1)!=arrIn.Length)
            {
                var rightNode = new Node(0);
                nodeIn.Right = rightNode;
                stack.Push(new Tuple<int[], Node>(arrIn[(midIndex+1)..], rightNode));
            }
        }
    }
    return node;
}

class Node
{
    public int Value {get;set;}
    public Node Left {get;set;}
    public Node Right {get;set;}

    public Node(int value, Node left = default, Node right = default)
    {
        this.Value = value;
        this.Left = left;
        this.Right = right;
    }

    public override string ToString()
    {
        return string.Format("({0},{1},{2})", this.Value, this.Left?.ToString(), this.Right?.ToString());
    }
}