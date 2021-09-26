using System;

namespace ReverseLinkedList
{
    class Node
    {
        public Node Next { get; set; }
        public int Value { get; set; }
    }

    class Solution
    {
        static Node GetLinkedList()
        {
            var node1 = new Node() { Value = 4 };
            var node2 = new Node() { Value = 3 };
            var node3 = new Node() { Value = 2 };
            var node4 = new Node() { Value = 1 };
            var node5 = new Node() { Value = 0 };

            node1.Next = node2;
            node2.Next = node3;
            node3.Next = node4;
            node4.Next = node5;

            return node1;
        }


        static Node ReverseLinkedList(Node list)
        {
            // TODO implement reversing the list
            var curNode = list;
            Node curNodePrev = null;

            while(curNode != null)
            {
                var next = curNode.Next;
                curNode.Next = curNodePrev;

                curNodePrev = curNode;
                curNode = next;
            }
            return curNodePrev;
        }

        static Node ReverseLinkedListRecursively(Node curr, Node prev)
        {
            if (curr == null) return null;

            Node next = curr.Next;
            curr.Next = prev;

            if (next == null)
                return curr;
            return ReverseLinkedListRecursively(next, curr);
        }

        static void PrintLinkedList(Node list)
        {
            var cur_node = list;
            while (cur_node != null)
            {
                Console.WriteLine("{0} ->", cur_node.Value);
                cur_node = cur_node.Next;
            }
        }

        static void Main(string[] args)
        {
            var list = GetLinkedList();
            Console.WriteLine("Initial list:");
            PrintLinkedList(list);
            var reverted = Solution.ReverseLinkedList(list);
            Console.WriteLine("Reverted list:");
            PrintLinkedList(reverted);

            var list2 = GetLinkedList();
            Console.WriteLine("Reverted (recursively) list:");
            var reverted2 = Solution.ReverseLinkedListRecursively(list2, null);
            PrintLinkedList(reverted2);
        }
    }
}