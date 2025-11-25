from typing import Optional, Tuple, Any

class HashTableOpenAddressing:
    def __init__(self, size=10):
        self.size = size
        # Hash table array: each slot can be either:
        # - None  → slot is empty
        # - (key, value) tuple → slot contains data
        # - self.deleted sentinel → slot used earlier but now deleted
        self.table: list[Optional[Tuple[Any, Any]]] = [None for _ in range(size)]
        
        # Unique object used as a "deleted marker" for open addressing
        # Helps us differentiate between an empty slot and a deleted slot
        self.deleted = object()
        
        
    def _hash(self, key):
        # Computes hash index within table range
        return hash(key) % self.size
    
    
    def insert(self, key, value):
        index = self._hash(key)          # First calculated index for the key
        original_index = index           # Save original index to detect full cycle
        first_deleted = None             # Track first deleted slot to reuse later
        
        while True:
            # Case 1: Empty slot found — good place to insert
            if self.table[index] is None:
                # If an earlier deleted slot was found, use it instead
                if first_deleted is not None:
                    index = first_deleted
                self.table[index] = (key, value)
                return
            
            # Case 2: Found a deleted slot — remember it if first one
            elif self.table[index] is self.deleted:
                if first_deleted is None:
                    first_deleted = index

            # Case 3: Key already exists — update the value
            elif self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            
            # Otherwise, keep probing (linear probing)
            index = (index + 1) % self.size
            
            # If we loop back to original index → table is full
            if index == original_index:
                raise Exception("Hash table is full")
            
            
    def get(self, key):
        index = self._hash(key)        # Starting search index
        original_index = index         # Track full loop
        
        # Continue until we hit an unused (None) slot
        while self.table[index] is not None:
            
            # Valid data slot AND keys match → return value
            if self.table[index] is not self.deleted and self.table[index][0] == key:
                return self.table[index][1]
            
            # Otherwise, move to next slot
            index = (index + 1) % self.size
            
            # Avoid infinite loop
            if index == original_index:
                break
        
        # Key not found
        return None 
    
    
    def delete(self, key):
        index = self._hash(key)
        original_index = index
        
        # Keep searching until empty slot found
        while self.table[index] is not None:
            
            # If valid data slot and key matches — mark it as deleted
            if self.table[index] is not self.deleted and self.table[index][0] == key:
                self.table[index] = self.deleted
                return True
            
            index = (index + 1) % self.size
            
            # Break if we loop around
            if index == original_index:
                break 
        
        # Key not found
        return False 
    
    
    def __str__(self):
        # Simple string representation of the table
        return str(self.table)
            
            
# --- Demo ---
ht = HashTableOpenAddressing(size=7)
ht.insert("apple", 10)
ht.insert("banana", 20)
ht.insert("orange", 30)
ht.insert("melon", 40)
ht.insert("grape", 50)

print(ht)
print("banana →", ht.get("banana"))

ht.delete("banana")
print(ht)
print("banana →", ht.get("banana"))
