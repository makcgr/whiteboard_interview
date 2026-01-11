// Пример дерева из картинки:
//          3
//        /   \
//      3      3
//     / \      \
//    2   3      3
//   / \
//  1   2

TreeNode root = new TreeNode(3);
root.Left = new TreeNode(3, new TreeNode(2, new TreeNode(1), new TreeNode(2)), new TreeNode(3));
root.Right = new TreeNode(3, null, new TreeNode(3));

Solution s = new Solution();
Console.WriteLine(s.LongestUnivaluePath(root)); // result: 4

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
    private int maxLen = 0;
    public int LongestUnivaluePath(TreeNode root)
    {
        maxLen = 0;
        DFS(root);
        return maxLen;
    }

    private int DFS(TreeNode? node)
    {
        if (node == null) return 0;
        int left = DFS(node.Left);
        int right = DFS(node.Right);

        int leftPath = (node.Left != null && node.Left.Value == node.Value)
            ? left + 1 : 0;
        int rightPath = (node.Right != null && node.Right.Value == node.Value)
            ? right + 1 : 0;
        maxLen = Math.Max(maxLen, leftPath + rightPath);
        return Math.Max(leftPath, rightPath);
    }
}