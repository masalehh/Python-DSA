class Hashtable:
    """Initialize the hash table with a fixed number of buckets."""
    def __init__(self, size=10) -> None:
        self.size = size
        self.table = [[] for _ in range(size)] 
        
        
    def _hash(self, key):
        """Hash function: converts a key into a bucket index."""
        return hash(key) % self.size 
    
    
    def insert(self, key, value):
        """Insert or update the key-value pair."""
        index = self._hash(key) 
        bucket = self.table[index] 
      
      # Check if the key already exists → update
        for i, (k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
            
        # If key doesn't exist → append new pair
        bucket.append((key, value)) 
        
    
    
    def get(self, key):
        """Retrieve the value for a given key. Returns None if not found."""
        index = self._hash(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return v 
        return None     # Key not found
    
    
    def delete(self, key):
        """Remove the key-value pair from the table."""
        index = self._hash(key)
        bucket = self.table[index]
        
        for i, (k,v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True 
        return False 
    
    
    def __str__(self) -> str:
        """Readable string representation of the hash table."""
        return "\n".join(f"{i}: {bucket}" for i, bucket in enumerate(self.table))
    
    
    
# Example usage:
ht = Hashtable(size=5)
ht.insert("apple", 10)

ht.insert("banana", 20)
ht.insert("orange", 30)
ht.insert("banana", 25)  # Updates value for "banana"

print(ht.get("banana"))  # Output: 25
print(ht.get("grape"))   # Output: None
print(ht)
#ht.delete("apple")
print("After delete apple: \n", ht)    



"""
Key Notes:
1. _hash() ensures the key maps to a valid bucket index.
2. insert() updates if the key exists, else appends new pair.
3. get() searches only the relevant bucket, not the whole table.
4. delete() removes only the matching key.
"""

