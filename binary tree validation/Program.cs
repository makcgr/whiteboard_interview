/*
Validate Binary Search Tree
Условие задачи:
Дано: корень бинарного дерева.
Необходимо: определить, является ли дерево корректным бинарным деревом поиска (BST).
Корректное BST:
	•	Все значения в левом поддереве любого узла строго меньше значения этого узла.
	•	Все значения в правом поддереве строго больше значения этого узла.
	•	Поддеревья также должны являться корректными BST.

Вход:
    2
   / \
  1   3

Выход: true

Вход:
    5
   / \
  1   4
     / \
    3   6

Выход: false
*/

var tree1 = new TreeNode(2, new TreeNode(1), new TreeNode(3));
Console.WriteLine(IsValidBST(tree1));

var tree2 = new TreeNode(5, new TreeNode(1), new TreeNode(4, new TreeNode(3), new TreeNode(6)));
Console.WriteLine(IsValidBST(tree2));

static bool IsValidBST(TreeNode root)
{
    return IsValidBSTRec(root, null, null);
}

static bool IsValidBSTRec(TreeNode node, int? min, int? max)
{
    if (node == null)
        return true;

    if (min.HasValue && node.Value <= min.Value || max.HasValue && node.Value >= max)
        return false;

    return IsValidBSTRec(node.Left, min, node.Value) && IsValidBSTRec(node.Right, node.Value, max);
}

public class TreeNode
{
    public int Value { get; set; }
    public TreeNode? Left { get; set; }
    public TreeNode? Right { get; set; }

    public TreeNode(int value, TreeNode? left, TreeNode? right)
    {
        Value = value;
        Left = left;
        Right = right;
    }

    public TreeNode(int value)
    {
        Value = value;
    }
}



