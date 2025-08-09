# A simple tree where a node can have any number of childs

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value 
        self.children = []  # List of child nodes 
        
        
    def add_child(self, child_node):
        """Adds a child to this node"""
        self.children.append(child_node)
        
        
    def display(self, level=0):
        """Recursively prints the tree structure""" 
        print("   " * level + str(self.value))
        for child in self.children:
            child.display(level + 1)
            


root = TreeNode("Root")
child1 = TreeNode("Child 1")
child2 = TreeNode("Child 2")

child1.add_child(TreeNode(" child1: Grand Child 1 "))
child1.add_child(TreeNode(" child1: Grand Child 2  "))
child2.add_child(TreeNode(" child2: Grand Child 1 "))
child2.add_child(TreeNode(" child2: Grand Child 2  "))


root.add_child(child1)
root.add_child(child2)


root.display() 


""" root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)

root.add_child(child1)
root.add_child(child2)
child1.add_child(TreeNode(4))
child1.add_child(TreeNode(5))
child2.add_child(TreeNode(6))
child2.add_child(TreeNode(7))

root.display() 
 """