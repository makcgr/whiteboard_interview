# Implement your own hashtable
# Hashtable should operate with key-value pairs of (string, string)
#  Operations: add (key, value); search(key); remove(key)
#  Implementation: simple one - array(of indexes), dictionary (of references to linked list of key-value pairs)
#  Methods: 
#   sub add(key, value)
#   sub search(key)
#   sub remove(key)

class MyValue:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashtable:
    def __init__(self) -> None:
        self.dict = {} 

    def compute_hash(key):
        # add up first 5 char positions of key in ASCII, this will be the key
        ascii_sum = 0
        for i in range(0,4):
            ascii_sum += ord(key[i])
        return ascii_sum

    def add(self, key, value):
        if not isinstance(key, str) or not isinstance(value, str):
            raise ValueError("Not a string value!")
        if len(key) < 5:
            raise ValueError("Key is too short")
        if len(value) == 0:
            raise ValueError("Value is empty")

        new_val = MyValue(key, value)
        ix = MyHashtable.compute_hash(key)
        if ix in self.dict:
            a_val = self.dict[ix]
            if a_val.next == None:
                if a_val.key == key:
                    raise ValueError("The key already exists!")
            else:
                while a_val.next != None:
                    if a_val.key == key:
                        raise ValueError("The key already exists!")
                    a_val = a_val.next
            a_val.next = new_val
        else:
            self.dict[ix] = new_val

    def lookup(self, key):
        if not isinstance(key, str):
            raise ValueError("key is not a string!")
        if len(key) == 0:
            raise ValueError("key is empty string!")

        ix = MyHashtable.compute_hash(key)
        if ix not in self.dict:
            return None

        dict_val = self.dict[ix]
        while dict_val != None or dict_val.key != key:
            dict_val = dict_val.next
        return dict_val

    def remove(self, key):
        ix = MyHashtable.compute_hash(key)
        if ix not in self.dict:
            raise ValueError("No such key!")

        dict_val = self.dict[ix]
        prev = None
        while dict_val.key != key or dict_val.next != None:
            prev = dict_val
            dict_val = dict_val.next   
        if dict_val.key == key:
            if prev != None:
                prev.next = dict_val.next
            if dict_val == self.dict[ix]:
                self.dict[ix] = dict_val.next
        else:
            raise ValueError("No such key!")

# Tests
import unittest

class MyHashTableTest(unittest.TestCase):
    def testAddGoodKeysAndValues(self):
        ht = MyHashtable()
        ht.add("ABCDE", "Vashar Prokrationar")
        ht.add("BACDE", "Badri Shkartashvili")
        ht.add("ZZZZZ", "Misha Gavrilov")

        # dup value (ok)
        ht.add("ZZZZ1", "Misha Gavrilov")

    def testAddDupKey(self):
        ht = MyHashtable()
        ht.add("AAAAA","T1")

        with self.assertRaises(ValueError):
            ht.add("AAAAA","T2")

    def testAddKeyTooShortRaisesValueError(self):
        # key too short (nok)
        ht = MyHashtable()
        with self.assertRaises(ValueError):
            ht.add("A", "T3 T3")

    def testAddEmptyKeyRaisesValueError(self):
        ht = MyHashtable()
        with self.assertRaises(ValueError):
            ht.add("", "T4 T4")

    def testAddEmptyValueRaisesValueError(self):
        # empty key (nok)
        ht = MyHashtable()
        with self.assertRaises(ValueError):
            ht.add("AAAAA", "")


# TODO: a) tests for lookup b) tests for removal
# Test data
#    AAAA1 T1
#    AAA1A T2
#    AA1AA T3
#    BBBB1 T4
#    BBB1B T5 
#    CCCCC T6 
#
# a) Lookup tests
# - lookup for AAAA1 returs T1
# - lookup for AA1AA returs T3
# - lookup for ZZZZZ returns None
# - lookup for None raises ValueError
# - lookup for "" raises ValueError
#
# b) tests for removal
# - remove the key AAAA1 - leaves AAA1A and AA1AA in same dict slot
# - remove the key AAA1A - leaves AAAA1 and AA1AA in same dict slot
# - remove CCCCC - removes the slot completely

if __name__ == '__main__':
    unittest.main(argv=['ignored'], exit=False)