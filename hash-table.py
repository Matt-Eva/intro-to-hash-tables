class HashTable:

    def __init__(self, size):
        self.buckets = [None] * size

    def simple_hash(self, key):
        return len(key)

    def better_hash(self, key):
        hash_val = 0
        length = len(self.buckets)
        for char in key:
            char_val = ord(char)
            hash_val = hash_val + char_val % length
            if hash_val > lenght:
                