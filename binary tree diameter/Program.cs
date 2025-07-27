// Пример дерева:
//       1
//      / \
//     2   3
//    / \     
//   4   5   

TreeNode root = new TreeNode(1);
root.Left = new TreeNode(2);
root.Right = new TreeNode(3);
root.Left.Left = new TreeNode(4);
root.Left.Right = new TreeNode(5);
Console.WriteLine(new Solution().Diameter(root)); // 3

public class TreeNode
{
    public int Val { get; set; }
    public TreeNode? Left { get; set; }
    public TreeNode? Right { get; set; }
    public TreeNode(int val = 0, TreeNode? left = null, TreeNode? right = null)
    {
        this.Val = val;
        this.Left = left;
        this.Right = right;
    }
}

public class Solution
{
    private int maxDiameter = 0;

    public int Diameter(TreeNode root)
    {
        maxDiameter = 0;
        DFS(root);
        return maxDiameter;
    }

    private int DFS(TreeNode? node)
    {
        if (node == null)
            return 0;

        int leftHeight = DFS(node.Left);
        int rightHeight = DFS(node.Right);

        // обновляем максимальный диаметр:
        maxDiameter = Math.Max(maxDiameter, leftHeight + rightHeight);

        // возвращаем высоту текущего поддерева
        return 1 + Math.Max(leftHeight, rightHeight);
    }
}