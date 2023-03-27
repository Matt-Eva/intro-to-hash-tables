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
            self.head = Node(key, val)
            return val
        current_node = self.head
        if current_node.key == key:
                current_node.val = val
                return val
        while current_node.next_node != None:
            if current_node.key == key:
                current_node.val = val
                return val
            current_node = current_node.next_node
        current_node.next_node = Node(key, val)
        return val
    
    def delete(self, key):
        if self.head == None:
            return false
        current_node = self.head
        if current_node.key == key:
            if current_node.next_node != None:
                self.head = current_node.next_node
                return true
            else:
                self.head = None
                return true
        while current_node.next_node != None:
            if current_node.next_node.key == key:
                if current_node.next_node.next_node != None:
                    new_next_node = current_node.next_node.next_node
                    current_node.next_node.next_node = None
                    current_node.next_node = new_next_node
                    return true
                else:
                    current_node.next_node = None
                    return true
            current_node = current_node.next_node
        return false


    def get(self, key):
        if self.head == None:
            return false
        if self.head.key == key:
            return self.head.val
        current_node = self.head
        while current_node.next_node != None:
            if current_node.next_node.key == key
                return current_node.next_node.val
            current_node = current_node.next_node
        return false


class HashTable:

    def __init__(self, size):
        self.buckets = [LinkedList()] * size
        self.capacity = len(self.buckets)

    def simple_hash(self, key):
        return len(key)

    def better_hash(self, key):
        hash_val = 0
        key_len = len(key)
        i = 0
        while i < key_len:
            char_val = ord(key[i])
            hash_val += (char_val + i)**2
            i+=1
        return hash_val

    def get_index(self, key):
        hash_val = self.better_hash(key)
        index = hash_val % self.capacity
        return index

    def set_key(self, key, value):

    def get(self, key):
        index = get_index(key)
        return self.buckets[index].get(key)
                