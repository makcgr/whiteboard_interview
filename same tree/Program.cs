/*
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
*/

#pragma warning disable 8604
using System.Diagnostics;

// array of tuples of TreeNode
var testCases = new(TreeNode, TreeNode, bool) [] 
{
    (
        new TreeNode(1,new TreeNode(2),new TreeNode(3)),
        new TreeNode(1,new TreeNode(2),new TreeNode(3)),
        true
    ),
    (
        new TreeNode(1,new TreeNode(2),null),
        new TreeNode(1,null,new TreeNode(2)),
        false
    ),
    (
        new TreeNode(1,new TreeNode(2),new TreeNode(1)),
        new TreeNode(1,new TreeNode(1),new TreeNode(2)),
        false
    )
};

var sol = new Solution();
var i = 0;
foreach(var tc in testCases)
{
    Console.WriteLine($"Test {++i} (expected {tc.Item3})");
    Console.WriteLine($"Recursive: {sol.IsSameTreeRecursive(tc.Item1,tc.Item2)}");
    Console.WriteLine($"Iterative: {sol.IsSameTreeIterative(tc.Item1,tc.Item2)}\n");
};

// Definition for a binary tree node.
public class TreeNode {
    public int Val {get;set;}
    public TreeNode Left {get;set;}
    public TreeNode Right {get;set;}

    public TreeNode(int val=0) {
        this.Val = val;
    }
    public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
        this.Val = val;
        this.Left = left;
        this.Right = right;
    }
}

public class Solution {
    /*
    
    */
    public bool IsSameTreeRecursive(TreeNode p, TreeNode q) {
        if(p==null || q==null)
        {
            return (p == null && q==null);
        }
        if (p.Val!=q.Val) return false;
         
        return IsSameTreeRecursive(p.Left, q.Left) && IsSameTreeRecursive(p.Right, q.Right);
    }
    
    public bool IsSameTreeIterative(TreeNode? p, TreeNode? q) {
        
        var pStack = new Stack<TreeNode>();
        pStack.Push(p);
        var qStack = new Stack<TreeNode>();
        qStack.Push(q);    
        
        // Stack allows null values, so Count property will be the same for both pStack and qStack
        while (pStack.Count>0 && qStack.Count>0)
        {   
            p = pStack.Pop();
            q = qStack.Pop();
            
            if(p==null || q==null)
            {
                if (!(p == null && q==null))
                    return false;
            }
            else
            {
                if (p.Val!=q.Val) return false;

                pStack.Push(p.Left); 
                qStack.Push(q.Left);

                pStack.Push(p.Right); 
                qStack.Push(q.Right);
            }
        }
        return true;
    }
}