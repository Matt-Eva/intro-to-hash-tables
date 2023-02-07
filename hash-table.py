class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next_node = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, key, val):
        if self.head == None:
            self.head = Node.new(key, val)
        else:
            current_node = self.head
            while current_node.next_node != None:
                if current_node.key == key:
                    current_node.val = val
                else:
                    
                current_node = current_node.next_node
            current_node.next_node = Node.new(key, val)
    
    def 

class HashTable:

    def __init__(self, size):
        self.buckets = [None] * size
        self.capacity = self.buckets.length

    def simple_hash(self, key):
        return len(key)

    def better_hash(self, key):
        hash_val = 0
        key_len = len(key)
        i = 0
        while i < key_len:
            char_val = ord(key[i])
            hash_val += (char_val + i)**2
        return hash_val

    def get_index(self, key):
        hash_val = self.better_hash(key)
        index = hash_val % self.capacity
        return index

    def set_key(self, key, value):


    def get(self, key):
        index = get_index(key)
        return self.buckets[index]
                