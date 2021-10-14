using System;

TestSplitBST();

static void TestSplitBST()
{
    var n2 = new Node(2, null, null);
    var n1 = new Node(1, null, n2);

    var n5 = new Node(5, null, null);
    var n4 = new Node(4, null, n5);

    var root = new Node(3, n1, n4);

    Console.WriteLine("Before split:{1}{0}{1}", root, Environment.NewLine);

    var res = SplitBSTRec(root, 2);
    Console.WriteLine("After split:{1}{0}{1}", res, Environment.NewLine);

}

// s = split value
static Tuple<Node, Node> SplitBSTRec(Node node, int s)
{
    // if there are no children:
    if(node.Left==null && node.Right==null)
        return node.Value <= s ?
            new Tuple<Node, Node>(node, null) : new Tuple<Node, Node>(null, node);

    Node leftPart = null, rightPart = null;
    if(node.Value <= s)
    {
        // node.Left: these elements are all already <= s
        // for the right part: there may be elements >s and <=s, so we split
        var result = SplitBSTRec(node.Right, s);

        node.Right = result.Item1; // items < s, though > node.Value
        leftPart = node;
     
        rightPart = result.Item2; // items > s
    }
    else //node.Value > s
    {
        // node.Right: these elements are all already > s
        // for the left part: there may be elements <=s and <s, so we split   
        var result = SplitBSTRec(node.Left, s);

        node.Left = result.Item2; // these are > s but < node.Value
        rightPart = node;

        leftPart = result.Item1; // these are <= s
    }
    return new Tuple<Node, Node>(leftPart, rightPart);
}


class Node
{
    public int Value { get; set; }
    public Node Left { get; set; }
    public Node Right { get; set; }

    public Node(int value, Node left, Node right)
    {
        this.Value = value;
        this.Left = left;
        this.Right = right;
    }

    public override string ToString()
    {
        return string.Format("({0},{1},{2})",
            Value.ToString(),
            Left?.ToString() ?? "None",
            Right?.ToString() ?? "None");
    }
}
