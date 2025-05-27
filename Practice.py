#print ("hello world")
#print (10<1)
#print ("snake" == "cat")
#print ("A" > "B")
#print (not  15 < 11)
#print(not 32==30+1)

#variable=10
#print(variable)
#print(variable==5*2)

#age = 38
#print( "LIONEL'S AGE IS" ,19*2== age)
#myname="lionel">="Ssengooba"
#print("Lionel"<="MUSOKE")

#print ("Nairobi"<"Milan" and "Nairobi">"Hanoi") #using and logical operator AND 
#print ("Nairobi"<"Milan" or "Nairobi">"Hanoi") #using and logical operator OR 
#myname="Lionel"
#print(not myname== "JONATHAN" and "THOMAS" or "PETER")

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def print_tree(self, level=0):
        print("  " * level + "|_" + self.data)  # Print current node
        for child in self.children:
            child.print_tree(level + 1)         # Recursively print children

# Build the tree
if __name__ == "__main__":
    root = TreeNode("A")       # Root node
    b = TreeNode("B")
    c = TreeNode("C")
    d = TreeNode("D")
    e = TreeNode("E")

    root.add_child(b)          # A → B
    root.add_child(c)          # A → C
    b.add_child(d)             # B → D
    b.add_child(e)             # B → E

    # Print the tree structure
    print("Tree Structure:")
    root.print_tree()


