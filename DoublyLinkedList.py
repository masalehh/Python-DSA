class Node:
    """A node creation class in a doubly linked list."""
    def __init__(self, value) -> None:
        self.value = value 
        self.prev = None 
        self.next = None 
        
        

class DoublyLinkedList:
    """Implement doubly linked list using python language"""
    def __init__(self) -> None:
        self.head = None 
        self.tail = None 
        self.size = 0 
        
        
    def insert_at_head(self, insert_value):
        """Insert a new node at the beginning."""
        new_node = Node(insert_value)
        if not self.head:
            self.head = self.tail = new_node 
        else:
            new_node.next = self.head 
            self.head.prev = new_node
            self.head = new_node
        self.size += 1 
        
        
    def insert_at_tail(self, insert_value):
        """Insert a new node at the end."""
        new_node = Node(insert_value)
        if not self.tail:
            self.head = self.tail = new_node
            
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node 
        self.size += 1 
        
        
    def insert_at_position(self, insert_value, insert_at_position):
        """Insert at any position (0-based index)."""
        if 0 <= insert_at_position <= self.size:
            if insert_at_position == 0:
                self.insert_at_head(insert_value)
                return
            
            if insert_at_position == self.size:
                self.insert_at_tail(insert_value)
                return 
            
            new_node = Node(insert_value)
            current_node = self.head 
            for _ in range(insert_at_position - 1):
                current_node = current_node.next
            
            new_node.next = current_node.next 
            new_node.prev = current_node 
            current_node.next.prev = new_node
            current_node.next = new_node 
            self.size += 1 
            
        else:
            raise IndexError("Position out of range")
    
    
    def traverse_display(self):
        """Display linked list forward."""
        current_node = self.head
        while current_node:
            print(current_node.value, end="->")
            current_node = current_node.next 
        print("None")
        
        
    def traverse_display_reverse(self):
        """Display linked list backward."""
        current_node = self.tail 
        while current_node:
            print(current_node.value, end="->")
            current_node = current_node.prev  
        print("None")
        
    
    def delete_at_head(self):
        """Delete the first node."""
        if self.head == self.tail is None:
            raise IndexError("Empty List")
        
        if self.head == self.tail:
            self.head = self.tail = None 
        else:
            self.head = self.head.next 
            self.head.prev = None 
        self.size -= 1 
        
        
    def delete_at_tail(self):
        """Delete the last node."""
        if self.head == self.tail is None:
            raise IndexError("Empty List")
        
        if self.head == self.tail:
            self.head = self.tail = None 
        else:
            self.tail = self.tail.prev 
            self.tail.next = None 
        self.size -= 1 
        
        
    def delete_at_position(self, delete_position):
        """Delete node at a specific position."""
        if delete_position < 0 or delete_position >= self.size:
            raise IndexError("Position out of range")
        
        if delete_position == 0:
            self.delete_at_head() 
            return 
        
        if delete_position == self.size - 1:
            self.delete_at_tail() 
            return 
        
        current_node = self.head 
        for _ in range(delete_position):
            current_node = current_node.next 
            
        current_node.prev.next = current_node.next 
        current_node.next.prev = current_node.prev 
        self.size -= 1 
        
        
    def search(self, key):
        """Search for a value, return index or -1 if not found."""
        current_node = self.head 
        search_value_index = 0 
        while current_node:
            if current_node.value == key:
                return search_value_index
            
            current_node = current_node.next 
            search_value_index += 1 
        return -1 
    
    
    def to_list(self):
        """Convert linked list to a Python list (forward)."""
        converted_list = [] 
        current_node = self.head 
        while current_node:
            converted_list.append(current_node.value)
            current_node = current_node.next 
        return converted_list
    
    def to_list_reverse(self):
        """Convert linked list to a Python list (backward)."""
        converted_list = [] 
        current_node = self.tail 
        while current_node:
            converted_list.append(current_node.value)
            current_node = current_node.prev 
        return converted_list
        
        
    def __len__(self):
        return self.size 
    
    
        
dll = DoublyLinkedList()
dll.insert_at_head(10)
dll.insert_at_tail(20)
dll.traverse_display() 
dll.insert_at_position(15, 1)
dll.insert_at_tail(25)
dll.traverse_display() 
dll.traverse_display_reverse()
print(dll.to_list_reverse())
