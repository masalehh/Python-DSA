
from typing import Generic, TypeVar, Optional 


T = TypeVar('T')

class Queue(Generic[T]):
    """A simple FIFO queue implementation using a Python list."""
    
    
    def __init__(self) -> None:
        self._items: list[T] = [] 
        
    def enqueue(self, element: T):
        """
        Add an item to the end of the queue.
        
        :param item: The element to be added.
        """
        self._items.append(element)
        
    
    def dequeue(self) -> T:
        """
        Remove and return the item from the front of the queue.
        
        :return: The element at the front of the queue.
        :raises IndexError: If the queue is empty.
        """
        if self.is_empty():
           raise IndexError("Dequeu from empty queue")
       
        return self._items.pop(0)
   
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        :return: True if empty, False otherwise.
        """
        return len(self._items) == 0 
    
    
    def peek(self) -> Optional[T]:
        """
        Return the front element without removing it.
        
        :return: The front element or None if empty.
        """
        if self.is_empty():
           raise IndexError("Peek from empty queue")
       
        return self._items[0]
    
    
    def size(self):
        """
        Return the number of items in the queue.
        
        :return: The size of the queue.
        """
        return len(self._items) 
        
    
    
    def __len__(self)->int:
        """Enable len(queue) syntax."""
        return self.size() 
        
    
    
    def __str__(self) -> str:
        """Return a string representation of the queue."""
        return "Queue: " + str(self._items) 
       
       


# Example usage 

if __name__ == "__main__":
    q = Queue[int]()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(50)
    print(q)            # Queue: [10, 20, 30, 50]
    print("Dequeu: ", q.dequeue())  # 10
    print("Peek: ", q.peek())     # 20
    q.enqueue(800)
    print(q.is_empty()) # False
    print(q)            # Queue: [20, 30, 50, 800]
    print(len(q))       # 4