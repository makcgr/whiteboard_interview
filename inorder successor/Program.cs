using System;
using System.Collections.Generic;
using System.Diagnostics;

Console.WriteLine("Hello");

var tree = new Node(5);
tree.Left = new Node(3, tree);
tree.Right = new Node(7, tree);
tree.Left.Left = new Node(2, tree.Left);
tree.Left.Right =  new Node(4, tree.Left);
tree.Right.Left = new Node(6, tree.Right);
tree.Right.Right= new Node(9, tree.Right);

var inorderSuccessor = GetInorderSuccessor(tree.Left); // for 3
Console.WriteLine($"Inorder successor for {tree.Left.Value}: {inorderSuccessor?.Value}");
Debug.Assert(inorderSuccessor.Value==4);

inorderSuccessor = GetInorderSuccessor(tree.Right); // for 7
Console.WriteLine($"Inorder successor for {tree.Right.Value}: {inorderSuccessor?.Value}");
Debug.Assert(inorderSuccessor.Value==9);
    
inorderSuccessor = GetInorderSuccessor(tree.Left.Right); // for 4
Console.WriteLine($"Inorder successor for {tree.Left.Right.Value}: {inorderSuccessor?.Value}");
Debug.Assert(inorderSuccessor.Value==5);

static Node GetInorderSuccessor(Node node)
{
    /*
        2 parts:
           - if node.Right is not null:
                - look in right subtree of node and find the minimal
                    - we need to explore each left subnode if present, the farthest will be the answer 
           - if node.Right is null:
                - look in parent nodes, find the one that is "left" for it's parent. 
                  Such parent's parent is the answer
    */
    if (node.Right is not null)
    {
        var curNode = node.Right;
        while(curNode.Left != null)
        {
            curNode = curNode.Left;
        }
        return curNode;
    }
    else
    {
        var checkParent = node;
        while(checkParent != null)
        {
            if(checkParent.Parent != null && checkParent.Parent.Left == checkParent)
            {
                return checkParent.Parent;
            }
            checkParent = checkParent.Parent;
        }
    }
    return null;
}

class Node
{
    public Node Left {get;set;}
    public Node Right {get;set;}
    public Node Parent {get;set;}
    public int Value {get;set;} 
    public Node(int value)
    {
        this.Value = value;
    }
    public Node(int value, Node parent = null)
    {
        this.Value = value;
        this.Parent = parent;
    }
}