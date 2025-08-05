class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 
        

class SinglyLinkedList:
    def __init__(self):
        self.head = None 
        
        
    #Traverse and Print the linked list 
    def traversePrint(self):
        currentNode = self.head 
        while currentNode:
            print(currentNode.value, end="->")
            currentNode = currentNode.next 
        print(" None")
        
        
    # Insert a new node at a specific index given by user as method parameter
    def insert_at(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head 
            self.head = new_node
            return 
        currentNode = self.head 
        position = 0 
        while currentNode and position < index-1:
            currentNode = currentNode.next 
            position += 1 
        
        if not currentNode:
            raise IndexError("Index out of bound")
        
        new_node.next = currentNode.next
        currentNode.next = new_node
        print(f"{value} inserted at index: {index}")
        
        
    # Remove an element from singly link list given by index 
    def remove_at(self, index):
        if self.head is None:
            raise IndexError("remove from empty list") 
        
        if index == 0:
            removedNode = self.head.value 
            self.head = self.head.next 
            print(f"{removedNode.value} removed from the list")
            return removedNode
        
        currentNode = self.head 
        position = 0 
        while currentNode.next and position < index - 1:
            currentNode = currentNode.next 
            position += 1 
            
        if not currentNode.next:
            raise IndexError("Index out of bounds")
        removedNode = currentNode.next 
        currentNode.next = currentNode.next.next 
        print(f"{removedNode.value} removed from the list")
        return removedNode.value 
    
    
    # Remove a value if it is in the list giver by user 
    def remove_value(self, value):
        if self.head is None:
            raise IndexError("Remove from the empty list")
        if value == self.head.value:
            self.head = self.head.next 
            print(f"{value} removed from the list")
            return 
        
        currentNode = self.head 
        while currentNode.next:
            if currentNode.next.value == value:
                print(f"{currentNode.next.value} removed from the list")
                currentNode.next = currentNode.next.next 
                return 
            currentNode = currentNode.next 
            raise ValueError("Value is not found in the list")
        
        
    # Sort the list ascending/descending order 
    def sort_asc(self):
        elements = [] 
        if self.head is None and self.head.next is None:
            return 
        currentNode = self.head 
        while currentNode:
            elements.append(currentNode.value)
            currentNode = currentNode.next 
        
        elements.sort() 
        
        currentNode = self.head 
        for value in elements:
            currentNode.value = value 
            currentNode = currentNode.next 
            
            
        # Return the number of nodes in the linked list 
    def size(self):
        count = 0 
        currentNode = self.head 
        while currentNode:
            count += 1 
            currentNode = currentNode.next 
        return count 
    
    
    # Allow len() function to be used in linekd list   
    def __len__(self):
        return self.size() 
    
    
    
    # Reverse the link list 
    def reverse(self):
        prev = None 
        currentNode = self.head 
        while currentNode:
            next_node = currentNode.next 
            currentNode.next = prev
            prev = currentNode
            currentNode = next_node 
        self.head = prev 
        
        
        
    # Search a value in linked list and return index of that value or -1 if not found 
    def search(self, value):
        currentNode = self.head 
        index = 0 
        while currentNode:
            if currentNode.value == value:
                print(f"{value} fount at index: {index}")
                return index 
            currentNode = currentNode.next 
            index += 1 
        return -1 
    
    
     # Convert the linked list into a pythn list 
    def to_list(self):
        result = []
        currentNode = self.head 
        while currentNode:
            result.append(currentNode.value)
            currentNode = currentNode.next 
        return result 
    
    
    # Check the linked list is empty or not, return True if empty otherwise False 
    def is_empty(self):
        return self.head is None 
    
    #String representation of the linked list 
    def __repr__(self):
        return "->".join(map(str, self.to_list())) + "->None"
    

if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.insert_at(0, 5)
    ll.insert_at(1, 3)
    ll.insert_at(2, 8)
    ll.insert_at(1, 1)
    print("Linked List after insertion:")
    ll.traversePrint()  

    print("After removing index 1:")
    ll.remove_at(1)
    ll.traversePrint()  # 5 -> 3 -> 8 -> None

    print("After sorting:")
    ll.sort_asc()
    ll.traversePrint()  # 3 -> 5 -> 8 -> None

    print("Size of linked list:", ll.size())

    print("After reversing:")
    ll.reverse()
    ll.traversePrint()  # 8 -> 5 -> 3 -> None

    print("Search for value 5:", ll.search(5))  # Should print the index
    print("Linked List as list:", ll.to_list())
    print("Is linked list empty?", ll.is_empty())

    print("Remove value 5:")
    ll.remove_value(5)
    ll.traversePrint()  # 8 -> 3 -> None
    ll.insert_at(2, 125)
    ll.insert_at(3, 70)
    ll.traversePrint()
    ll.sort_asc()
    ll.traversePrint()
    print("Length using len():", len(ll))
    print("String representation:", repr(ll))

    
    
    
         
    
    