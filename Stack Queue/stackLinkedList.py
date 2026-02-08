class Node:
    """
    A node in a singly linked list
    """
    def __init__(self, value):
        self.value = value 
        self.next = None 
        
        
class Stack:
    """
    Stack implementation using a singly linked list with python.
    using LIFO (Last In, First Out) principle.
    """
    def __init__(self):
        self._head = None 
        self._size = 0 
        
    def is_empty(self):
        """Return True if the stack is empty, False otherwise."""
        return self._size == 0 
    
    def push(self, element):
         """Push an element onto the top of this stack."""
         new_node = Node(element)
         new_node.next = self._head
         self._head = new_node
         self._size += 1 
         print(f"{element} Pushed into Stack")
         
    def pop(self):
        """Remove and return the top element of the stack.
        Raises IndexError if the stack is empty."""
        if self.is_empty():
            raise IndexError("Cannot pop from empty stack")
        
        popped_node = self._head
        self._head = self._head.next 
        self._size -= 1 
        print(f"Popped: {popped_node.value}")
        return popped_node.value 
    
    def peek(self):
        """Return the top element from stack without removing it.
        Raises IndexError if the stack is empty."""
        if self.is_empty():
            raise IndexError("Cannot peek from empty stack")
        return self._head.value 
    
    def size(self):
        """Return the number of elements in the stack."""
        return self._size
    
    def __len__(self):
        return self._size
    
    def __repr__(self):
        """Return a string representation of the stack from top to bottom."""
        if self.size() == 0:
            return "Stack is Empty so nothing to print"
        
        nodes = [] 
        current = self._head
        while current:
            nodes.append(repr(current.value))
            current = current.next 
        return "Stack(top->bottom): " + " -> ".join(nodes)
    
    
if __name__ == "__main__":
    # Some example usage for the above code
    stack = Stack() 
    stack.push(17)
    stack.push(20)
    stack.push(94)
    print(stack)                    # This internally calls stack.__repr__()
    print("Peek:", stack.peek())    # Peek: 30
    print("Size:", stack.size())    # Size: 3
    stack.pop()                     # Popped: 30
    print("After pop:", stack)      # Stack(top->bottom): 20 -> 10
    
    # Pop remaining elements
    stack.pop()                     # Popped: 20
    stack.pop()                     # Popped: 10
    print(stack)
    
    # Uncommenting the next line will raise an error
    # stack.pop()
    
    
    #End of the Program 
    