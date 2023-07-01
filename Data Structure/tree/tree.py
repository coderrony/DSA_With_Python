
class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preOrder(root):
    if root:
        print(root.data, end=" ")

        preOrder(root.left)

        preOrder(root.right)


def inOrder(root):

    if root is not None:
        inOrder(root.left)

        print(root.data, end=" ")

        inOrder(root.right)


def postOrder(root):

    if root is not None:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=" ")


root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)


# preOrder(root)
# print(end="\n")
# inOrder(root)
# postOrder(root)

