class DoctorNode:
    def __init__(self, name):
        self.name = name #stores doctor name
        self.left = None #references to the left
        self.right = None #references to the right

class DoctorTree:
    def __init__(self): #creating empty list initially
       self.root = None
    def find_node (self, current, name):
        if current is None:
            return None
        if current.name == name:
            return current
        #searching left subtree
        found = self.find_node(current.left, name)
        if found: 
            return found
        #searching right subtree
        return self.find_node(current.right, name)
    #insert method
    def insert(self, parent_name, doctor_name, side):
        parent = self.find_node(self.root, parent_name)
        if parent is None:
            print(f"{parent_name} not found. ")

        new_doctor = DoctorNode(doctor_name)
        if side == "left":
            parent.left = new_doctor #left side
        elif side == "right": 
            parent.right = new_doctor #right side
        else:
            print("Side must be 'left' or 'right'.")
    
    #preorder traversal
    def preorder (self, node):
        if node is None:
            return []
        return (
            [node.name] #Root
            + self.preorder(node.left) #Left
            + self.preorder(node.right) #Right
        )
    #inorder traversal
    def inorder(self, node):
        if node is None:
            return []
        return (
            self.inorder(node.left) #Left
            + [node.name] #Root
            + self.inorder(node.right) #Right
        )
    def postorder(self,node):
        if node is None:
            return []
        return (
            self.postorder(node.left)
            + self.postorder(node.right)
            + [node.name]
        )


# Test your DoctorTree and DoctorNode classes here
#NORMAL TESTING CASES: 
tree = DoctorTree()
tree.root = DoctorNode("Dr. Croft") 
# Insert values
tree.insert("Dr. Croft", "Dr. Goldsmith", "right") 
tree.insert("Dr. Croft", "Dr. Phan", "left")
tree.insert("Dr. Phan", "Dr. Carson", "right") 
tree.insert("Dr. Phan", "Dr. Morgan", "left")

print(tree.preorder(tree.root))
print (tree.inorder(tree.root))
print(tree.postorder(tree.root))

#EDGE TEST CASES
#tree.insert("Dr.Smith", "Dr.Who", "left")
#not left or right entered
#tree.insert("Dr.Croft", "Dr.Who", "where")

