class Node:
    """
    A node class to create a singly linked list node for queue
    """
    def __init__(self, value):
        self.value = value 
        self.next = None 
        

class Queue:
    """
    Queue implementation using singly linked list, queue follows FIFO (First In First Out)
    """
    def __init__(self):
        self._front = None 
        self._rear = None 
        self._size = 0 
    
    def is_empty(self):
        """Return True if queue is empty otherwise return False"""
        return self._size == 0 
    
    def enqueue(self, element):
        """
        Add an element end of the queue(rear)
        """
        new_node = Node(element)
        
        if self.is_empty():
            self._front = self._rear = new_node
        else:
            self._rear.next = new_node
            self._rear = new_node
        self._size += 1 
        
        
    def dequeue(self):
        """
        Remove and return the front element of the queue who comes first
        also Raised IndexError if queue is empty
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty queue")
        
        poppedNode = self._front  
        self._front = self._front.next 
        if self._front is None:
            self._rear = None 
        self._size -= 1 
        print(f"{poppedNode.value} dequeued from queue")
        return poppedNode.value 
    
    def peek(self):
        """Return front element of the queue, Raised IndexError if queue is empty"""
        if self.is_empty():
            raise IndexError("Cannot peek from empty queue")
        return self._front.value 
    

    def size(self):
        """Return size of the current queue"""
        return self._size 
    
    def __len__(self):
        """Return size of the queue"""
        return self._size 
    
    def __repr__(self):
        """Return string representation of the queue Top to bottom"""
        nodes = [] 
        current = self._front 
        while current:
            nodes.append(repr(current.value))
            current = current.next 
        return "Queue(Top->Bottom)" + "->".join(nodes)
    
    
    
if __name__ == "__main__":
    # Some Example usage
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(22)
    queue.enqueue(37)
    queue.enqueue(39)
    print(queue)                    # Queue(front->rear): 10 -> 22 -> 37 -> 39
    print(len(queue))
    print("Peek:", queue.peek())    # Peek: 10
    print("Size:", queue.size())    # Size: 4
    queue.dequeue()                 # Dequeued: 10
    print("After dequeue:", queue)  # Queue(front->rear): 22 -> 37 -> 39 
    queue.dequeue()                 # Dequeued: 22
    queue.dequeue()                 # Dequeued: 37
    print("After dequeue:", queue)  # Queue(front->rear): 39
    queue.dequeue()                 # Dequeued: 39
    
    # Uncommenting the next line will raise an error
    # queue.dequeue()
            