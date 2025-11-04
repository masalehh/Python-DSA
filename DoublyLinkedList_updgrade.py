from typing import Optional

class Node:
    """A node class in a doubly linked list."""
    def __init__(self, value) -> None:
        self.value = value
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None
        
    
class DoublyLinList_upgrde:
    """Doubly Linked List with Pythonic features."""
    def __init__(self) -> None:
        self.head = None 
        self.tail = None 
        self.size = 0 
        
        
# ----------------- Insertion Methods -----------------
    def insert_at_head(self, insert_value):
        new_node = Node(insert_value)
        
        if not self.head:
            self.head = self.tail = new_node  
        else:
            new_node.next = self.head 
            self.head.prev = new_node 
            self.head = new_node 
        self.size += 1 
        
    
    def insert_at_tail(self, insert_value):
        new_node = Node(insert_value)
        
        if not self.tail:
            self.head = self.tail = new_node 
             
        else:
            self.tail.next = new_node
            new_node.prev = self.tail 
            self.tail = new_node
        self.size += 1 
        
    
    def insert_at_pos(self, insert_value, insert_position):
        if 0 <= insert_position <= self.size:
            if insert_position == 0:
                return self.insert_at_head(insert_value) 
            
            if insert_position == self.size:
                return self.insert_at_tail(insert_value)
            
            new_node = Node(insert_value)
            current_node = self._get_node(insert_position - 1) 
            
            new_node.next = current_node.next 
            new_node.prev = current_node
            current_node.next = new_node
            new_node.next.prev = new_node
            self.size += 1 
              
        else:
            raise IndexError("Insert Position out of range") 
        
    
    
    def _get_node(self, index):
        """Helper: get node position at index (0-based)."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        
        # Optimize: traverse from head or tail depending on index
        if index < self.size // 2: 
            current_node = self.head 
            for _ in range(index):
                current_node = current_node.next 
            return current_node
        else:
            current_node = self.tail 
            for _ in range(self.size - index - 1):
                current_node = current_node.prev 
            return current_node
           
    
# ----------------- Deletion Methods -----------------
    def delete_at_head(self):
        if not self.head:
            raise IndexError("List is Empty")
        
        if self.head == self.tail:
            self.head = self.tail = None 
        else:
            self.head = self.head.next
            self.head.prev = None 
        self.size -= 1 
         
    
    def delete_at_tail(self):
        if not self.tail:
            raise IndexError("List is Empty") 
        
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev 
            self.tail.next = None 
        self.size -= 1 
        
        
    
    def delete_at_pos(self, del_position):
        if del_position < 0 or position >= self.size:
            raise IndexError("Position out of range")
        
        if del_position == 0:
            return self.delete_at_head()
        
        if del_position == self.size - 1:
            return self.delete_at_tail() 
        
        current_node = self._get_node(del_position)
        current_node.prev.next = current_node.next 
        current_node.next.prev = current_node.prev 
        self.size -= 1 
        
    
    
    # ----------------- Utility Methods -----------------
    def search(self, search_value):
        current_node = self.head 
        index = 0 
        while current_node:
            if current_node.value == search_value:
                return index 
            current_node = current_node.next 
            index += 1
        return -1  


    #------ Efficiently search value in linked list, writing by me ------------
    def search_optimized(self, value):
        # Start searching from the head (first node)
        search_value_index = 0

        # ✅ Step 1: Check if the head node contains the target value
        if self.head.value == value:
            return search_value_index  # Found at index 0 (head position)

        # ✅ Step 2: Check if the tail node contains the target value
        # This avoids unnecessary traversal if the value is at the end.
        elif self.tail.value == value:
            return self.size - 1  # Tail is always at index (size - 1)

        else:
            # ✅ Step 3: Search in the middle nodes only
            # Since head and tail are already checked, we start from head.next
            search_value_index = 1
            current_node = self.head.next

            # Loop until the node before the tail (since tail is already checked)
            while current_node.next:
                # If the current node's value matches, return its position
                if current_node.value == value:
                    return search_value_index

                # Move to the next node and increment index counter
                current_node = current_node.next
                search_value_index += 1

            # ✅ Step 4: If not found in any node, return -1 as "not found" signal
            return -1


    def to_list(self):
        return [node for node in self] 


    def to_list_reverse(self):
        return [node for node in reversed(self)] 


    # ----------------- Pythonic Methods -----------------
    def __len__(self):
        return self.size 
    

    def __iter__(self):
        current = self.head 
        while current:
            yield current.value 
            current = current.next 
            

    def __reversed__(self):
        current = self.tail 
        while current:
            yield current.value 
            current = current.prev 


    def __getitem__(self, index):
        return self._get_node(index).value


    def __setitem__(self, index, value):
        self._get_node(index).value = value 
        
        
    def __delitem__(self, index):
        self.delete_at_pos(index) 
            

    def __repr__(self):
        return " <-> ".join(str(x) for x in self)  + " <-> None"



# ----------------- Example Usage -----------------
dll = DoublyLinList_upgrde()
dll.insert_at_head(10)
print(dll)
dll.insert_at_tail(20)
print(dll)
dll.insert_at_tail(30)
dll.insert_at_pos(15, 1)

print(dll)  # 10 <-> 15 <-> 20 <-> 30 <-> None

print(list(dll))        # [10, 15, 20, 30]
print(list(reversed(dll)))  # [30, 20, 15, 10]

print("Length:", len(dll))  # 4
print("Search 20:", dll.search(20))  # 2
print("Optimized Search 15 at index: ", dll.search_optimized(15)) 