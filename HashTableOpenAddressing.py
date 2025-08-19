from typing import Optional, Tuple, Any

class HashTableOpenAddressing:
    def __init__(self, size=10):
        self.size = size 
        self.table: list[Optional[Tuple[Any, Any]]] = [None for _ in range(size)]  # Allows storing None or (key, value) tuples
        self.deleted = object() 
        
        
    def _hash(self, key):
        return hash(key) % self.size 
    
    
    def insert(self, key, value):
        index = self._hash(key)
        original_index = index 
        first_deleted = None 
        
        while True:
            if self.table[index] is None: 
                if first_deleted is not None: 
                    index = first_deleted 
                self.table[index] = (key, value)
                return 
            elif self.table[index] is self.deleted:
                if first_deleted is None:
                    first_deleted = index 
                    
            elif self.table[index][0] == key:
                self.table[index] = (key, value)
                return 
            
            index = (index + 1) % self.size 
            if index == original_index:
                raise Exception("Hash table is full")
            
            
    def get(self, key):
        index = self._hash(key)
        original_index = index 
        
        
        while self.table[index] is not None:
            if self.table[index] is not self.deleted and self.table[index][0] == key:
                return self.table[index][1]
            
            index = (index + 1) % self.size 
            if index == original_index:
                break 
        return None 
    
    
    
    def delete(self, key):
        index = self._hash(key)
        original_index = index 
        
        
        while self.table[index] is not None:
            if self.table[index] is not self.deleted and self.table[index][0] == key:
                self.table[index] = self.deleted
                return True 
            index = (index + 1) % self.size
            if index == original_index:
                break 
        return False 
    
    
    def __str__(self):
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

        