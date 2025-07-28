//      1
//     / \
//    2   3
//       / \
//      4   5

var root = new TreeNode(1,
    new TreeNode(2),
    new TreeNode(3, new TreeNode(4), new TreeNode(5))
);
var result = TreeSum(root); // 1 + 2 + 3 + 4 + 5 = 15
Console.WriteLine(result);

int TreeSum(TreeNode node)
{
    if (node == null) return 0;

    Queue<TreeNode> queue = new();
    queue.Enqueue(root);

    var sum = 0;
    while (queue.Count > 0)
    {
        var curr = queue.Dequeue();

        sum += curr.Value;
        if (curr.Left != null) queue.Enqueue(curr.Left);
        if (curr.Right != null) queue.Enqueue(curr.Right);
    }
    return sum;
}

public class TreeNode
{
    public int Value { get; set; }
    public TreeNode? Left { get; set; }
    public TreeNode? Right { get; set; }
    public TreeNode(int value = 0, TreeNode? left = null, TreeNode? right = null)
    {
        this.Value = value;
        this.Left = left;
        this.Right = right;
    }
}