var lRUCache = new LRUCache(2);
lRUCache.Put(1, 1);
var result1 = lRUCache.Get(1);

class LRUCache
{
    class Node
    {
        public int Key;
        public int Value;
        public Node Prev;
        public Node Next;

        public Node(int key, int value)
        {
            Key = key;
            Value = value;
        }
    }

    private int _capacity;
    private Dictionary<int, Node> _cache;
    private Node _head;
    private Node _tail;

    public LRUCache(int capacity)
    {
        _capacity = capacity;
        _cache = new Dictionary<int, Node>();
        _head = new Node(0, 0);
        _tail = new Node(0, 0);
        _head.Next = _tail;
        _tail.Prev = _head;
    }

    public int Get(int key)
    {
        if (_cache.ContainsKey(key))
        {
            var node = _cache[key];
            MoveToHead(node);
            return node.Value;
        }
        return -1;
    }

    public void Put(int key, int value)
    {
        if (_cache.ContainsKey(key))
        {
            var node = _cache[key];
            node.Value = value;
            MoveToHead(node);
        }
        else
        {
            var newNode = new Node(key, value);

            if (_cache.Count >= _capacity)
            {
                var tail = RemoveTail();
                _cache.Remove(tail.Key);
            }

            _cache[key] = newNode;
            AddToHead(newNode);
        }
    }

    private void AddToHead(Node node)
    {
        node.Prev = _head;
        node.Next = _head.Next;
        _head.Next.Prev = node;
        _head.Next = node;
    }
    
    private void RemoveNode(Node node)
    {
        node.Prev.Next = node.Next;
        node.Next.Prev = node.Prev;
    }

    private void MoveToHead(Node node)
    {
        RemoveNode(node);
        AddToHead(node);
    }
    
    private Node RemoveTail()
    {
        var lastNode = _tail.Prev;
        RemoveNode(lastNode);
        return lastNode;
    }
}