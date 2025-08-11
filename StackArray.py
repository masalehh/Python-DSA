
from typing import Generic, List, Optional, TypeVar 


T = TypeVar('T')


class Stack(Generic[T]):
    """
    A stack data structure (LIFO: Last-In, First-Out) implemented using a Python list.

    Methods:
        push(item): Add an item to the top of the stack.
        pop(): Remove and return the top item from the stack.
        peek(): Return the top item without removing it.
        is_empty(): Check if the stack is empty.
        size(): Return the number of items in the stack.
    """
    
    def __init__(self) -> None:
        """Initialize an empty stack."""
        self._items: List[T] = [] 
        
        
    def push(self, item:T) -> None: 
        """Push an item onto the stack."""
        self._items.append(item)
        
        
    def pop(self) -> Optional[T]:
        """
        Remove and return the top item from the stack.
        Returns None if the stack is empty.
        """
        if self.is_empty():
            return None 
        else: 
            return self._items.pop() 
        
        
    def peek(self) -> Optional[T]:
        """
        Return the top item without removing it.
        Returns None if the stack is empty.
        """
        if self.is_empty():
            return None 
        else: 
            return self._items[-1]
        
    
    def is_empty(self):
        """Check if the stack is empty."""
        return self.size() == 0 
    
    
    def size(self) -> int:
        """Return the number of items in the stack."""
        return len(self._items)
    
    
    def __repr__(self) -> str:
        """Return a string representation of the stack."""
        return f"Stack ({self._items})"
    
    
    
if __name__ == "__main__":
    stack = Stack[int]()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push('30')                # Generic warn me that it is different data type 
    print("Stack after pushes:", stack)
    print("Peek top item:", stack.peek())
    print("Pop item:", stack.pop())
    print("Stack after pop:", stack)
    print("Is empty?", stack.is_empty())
    print("Stack size:", stack.size())
    
    
        