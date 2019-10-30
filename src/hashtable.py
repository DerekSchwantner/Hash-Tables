# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index =  self._hash_mod(key)

        index = self._hash_mod(key)

        # check if key already exists, if not, create new LinkedPair
        if self.storage[index] == None:
            self.storage[index] = LinkedPair(key, value)
        else:
            current = self.storage[index]

            if current.key == key:
                current.value = value
                return

            while current.next:
                if current.next.key == key:
                    current.next.value = value
                    return

                else:
                    current = current.next
            # if check gets all the way through, chain a new LinkedPair on the end with the key, value
            current.next = LinkedPair(key, value)




    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        current_node = self.storage[index]
        if current_node:
            last_node = None
            # while the current node exists
            while current_node:
                if current_node.key == key:
                    # change pointer if last node is not None
                    if last_node:
                        last_node.next = current_node.next
                    else:
                        self.storage[index] = current_node.next
                last_node = current_node
                current_node = current_node.next
        else:
            # If you try to remove a value that isn't there, print a warning.
            print("Unable to remove item")
            # Should return None if the key is not found.
            return None


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        current_node = self.storage[index]
        while current_node:
            if current_node.key == key:
                return current_node.value
            else:
                current_node = current_node.next
        return None



    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_storage = [None] * self.capacity
        old_storage = self.storage
        self.storage = new_storage

        for i in old_storage:
            current_loop = i
            while current_loop:
                self.insert(current_loop.key, current_loop.value)
                current_loop = current_loop.next




if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
