class Tree:
    def __init__(self, cargo , left=None , right=None , root=None):
        self.cargo = cargo
        self.left = left
        self.right = right
        self.root = root

    def __str__(self):
        return 'this is a node with the cargo {self.cargo}, in a {self.root} tree'.format(self=self)
def Total(tree):
    if tree == None :
        return 0
    else :
        return Total(tree.left) + Total(tree.right) + tree.cargo


left = Tree(1)
right = Tree(3)
root = Tree(2)
ultraRoot = Tree(1)
ultraRoot.right = root
root.right = right
root.left = left

root.root = ultraRoot


print(Total(ultraRoot))
