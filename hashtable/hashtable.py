

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.length = 0
    
    def find(self, key):
        current = self.head

        while current is not None and current.key != key:
            current = current.next

        return current
    
    def insert_at_head(self, key, value):
        current = self.head

        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next

        new_entry = HashTableEntry(key, value)
        new_entry.next = self.head
        self.head = new_entry
        self.length += 1
    
    def remove(self, key):    
        current = self.head
        next_node = current.next
        if current.key == key:
            self.head = next_node
            self.length -= 1
            return current.value

        while next_node is not None:
            if next_node.key == key:
                removed = next_node
                current.next = next_node.next
                self.length -= 1
                return removed.value

            current = next_node
            next_node = current.next
        
        return None
        

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        # Your code here
        self.capacity = capacity
        self.storage = [None] * self.capacity
        self.max_load_factor = 0.7

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        entries = sum([x.length for x in self.storage if x])
        return entries / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        if self.get_load_factor() > self.max_load_factor:
            self.resize(self.capacity * 2)
        hash_index = self.hash_index(key)
        if self.storage[hash_index] is None:
            ll = LinkedList()
            ll.insert_at_head(key, value)
            self.storage[hash_index] = ll
        else: 
            self.storage[hash_index].insert_at_head(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        hash_index = self.hash_index(key)
        if self.storage[hash_index] is None:
            print("Key is not found.")
            return 
        else:
            return self.storage[hash_index].remove(key)


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        hash_index = self.hash_index(key)
        if self.storage[hash_index] is None:
            return None
        else:
            entry = self.storage[hash_index].find(key)
            if not entry:
                return None
            return entry.value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        old_table = self.storage
        self.storage = [None] * new_capacity
        self.capacity = new_capacity

        for x in old_table:
            if x:
                current = x.head
                while current is not None:
                    self.put(current.key, current.value)
                    current = current.next
        


        


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")
    ht.put("line_13", "And did some stuff.")
    ht.put("line_14", "And said goodbye.")
    ht.put("line_15", "And said hello.")
    ht.put("line_16", "And did something else.")
    ht.put("line_17", "blah blah blah.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 18):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    print("")
