// Find the maximum path sum
// Example:
//          1
//        /   \
//      2      3
//     / \      
//    3   2      
//
//  Answer: 9

TreeNode root = new TreeNode(1);
root.Left = new TreeNode(2, new TreeNode(3), new TreeNode(2));
root.Right = new TreeNode(3);

Solution s = new Solution();
Console.WriteLine(s.MaximumPathSum(root)); // result: 4

public class TreeNode
{
    public int Value;
    public TreeNode? Left;
    public TreeNode? Right;
    public TreeNode(int value)
    {
        Value = value;
    }

    public TreeNode(int value, TreeNode? left = null, TreeNode? right = null)
    {
        Value = value;
        Left = left;
        Right = right;
    }
}

public class Solution
{
    private int _maxPathSum = 0;
    public int MaximumPathSum(TreeNode root)
    {
        DFS(root);

        return _maxPathSum;
    }

    private int DFS(TreeNode? node)
    {
        if (node == null) return 0;

        var leftSum = node.Left != null ? DFS(node.Left) : 0;
        var rightSum = node.Right != null ? DFS(node.Right) : 0;

        var sum = node.Value + Math.Max(leftSum, rightSum);
        _maxPathSum = Math.Max(sum, _maxPathSum);

        return sum;
    }
}