class HashMap:
    def __init__(self, size=100):
        # The size of the hashmap is set during initialization. It determines the number of buckets in the hashmap.
        # By default, it's set to 100, but can be customized if needed.
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        # We use hash() function to generate a hash value for the key.
        # The modulus operation is applied to ensure that the hash value falls within the range of the size.
        hash_index = hash(key) % self.size
        return hash_index

    def put(self, key, value):
        hash_index = self._hash(key)
        for i, (k, v) in enumerate(self.table[hash_index]):
            if k == key:
                # Collisions are handled using separate chaining.
                # Each bucket in the hashmap contains a list of key-value pairs.
                # When a collision occurs, the new key-value pair is appended to this list.
                self.table[hash_index][i] = (key, value)
                return
        self.table[hash_index].append((key, value))

    def get(self, key):
        hash_index = self._hash(key)
        for k, v in self.table[hash_index]:
            if k == key:
                return v
        return None


def test_hashmap():
    hashmap = HashMap()
    hashmap.put('five', 5)
    hashmap.put('ten', 10)

    assert hashmap.get('five') == 5
    assert hashmap.get('ten') == 10
    assert hashmap.get('one') is None

    hashmap.put('five', 7)
    assert hashmap.get('five') == 7


if __name__ == "__main__":
    test_hashmap()
