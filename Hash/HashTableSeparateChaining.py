class HashMap:
    def __init__(self, initial_capacity=8) -> None:
        """
        Initialize the hash map with a given capacity.
        Uses separate chaining — each bucket is a list to handle collisions.

        Args:
            initial_capacity (int): initial number of buckets (default=8)

        Time Complexity: O(n)  — for creating n empty buckets
        Space Complexity: O(n) — proportional to capacity
        """
        self.size = 0 
        self.capacity = initial_capacity
        self.buckets = [[] for _ in range(self.capacity)]  # list of buckets (chaining)
        
    def _hash(self, key):
        """
        Compute the hash index for a given key.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return hash(key) % self.capacity
    
    
    def put(self, key, value):
        """
        Insert or update a key-value pair in the hash map.
        If key already exists, update its value.
        If load factor > 0.75, trigger rehashing.

        Average Time Complexity: O(1)
        Worst-case Time Complexity: O(n)  — if all elements fall into one bucket
        Space Complexity: O(1) (amortized)
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        
        # Update existing key if found
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return 
        
        # Otherwise, add new pair
        bucket.append((key, value))
        self.size += 1 
        
        # Maintain load factor threshold (0.75)
        if self.size / self.capacity > 0.75:
            self._rehash() 
            
            
    def get(self, key):
        """
        Retrieve the value for a given key.
        Returns None if key not found.

        Average Time Complexity: O(1)
        Worst-case Time Complexity: O(n)
        Space Complexity: O(1)
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for k, v in bucket:
            if k == key:
                return v 
        return None 
    
    
    def remove(self, key):
        """
        Remove a key-value pair from the hash map if it exists.

        Average Time Complexity: O(1)
        Worst-case Time Complexity: O(n)
        Space Complexity: O(1)
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        
        # ❌ BUG FIX: enumerate needs index+value tuple unpacking
        for i, (k, v) in enumerate(bucket):  
            if k == key:
                del bucket[i]
                self.size -= 1 
                return True 
        return False 
    
    
    def _rehash(self):
        """
        Double the capacity and reinsert all key-value pairs.
        Maintains O(1) average-time operations by controlling load factor.

        Time Complexity: O(n) — all items reinserted
        Space Complexity: O(n) — new bucket array allocated
        """
        old_buckets = self.buckets
        self.capacity *= 2 
        self.buckets = [[] for _ in range(self.capacity)] 
        self.size = 0 
        
        # Reinserting existing key-value pairs into new bucket layout
        for bucket in old_buckets:
            for k, v in bucket:
                self.put(k, v) 
                

# Example Usage
hm = HashMap()
hm.put("name", "Saleh")
hm.put("age", 25)

print(hm.get("name"))   # Output: Saleh
print(hm.get("age"))    # Output: 25
