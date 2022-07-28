/*
Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Ex:
Input: root = [3,9,20,null,null,15,7]
        3
      /   \
    9       20
          /   \
        15      7

Output: 3

-----------------

Solution:

We need to perform recursive search into the depth of the tree to find the most deep node of the tree.
We will pass the current node as a parameter along with the current depth to DepthSearch method 
 which will recursively return the current established depth. 
*/


var tree = new TreeNode(3, new TreeNode(9), new TreeNode(20, new TreeNode(15), new TreeNode(7)));
Console.WriteLine("Maximum depth of BT is {0}", Solution.GetMaximumDepthOfBT(tree));

public class Solution
{
    public static int GetMaximumDepthOfBT(TreeNode root)
    {
        return DepthSearch(root, 0);
    }

    private static int DepthSearch(TreeNode node, int curDepth)
    {
        if (node == null) return curDepth;
        curDepth++;

        return Math.Max(DepthSearch(node.Left, curDepth), DepthSearch(node.Right, curDepth));
    }
}

public class TreeNode
{
    public int Value {get;set;}
    public TreeNode Left { get; set; }
    public TreeNode Right { get; set; }

    public TreeNode(int value)
    {
        this.Value = value;
    }

    public TreeNode(int value, TreeNode left, TreeNode right)
    {
        this.Value = value;
        this.Left = left;
        this.Right = right;
    }
}


