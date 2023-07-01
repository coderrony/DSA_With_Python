
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def isFullBinaryTree(root):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return True

    if root.left is not None and root.right is not None:
        return isFullBinaryTree(root.left) and isFullBinaryTree(root.right)

    return False


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)

root.right.left = Node(5)
root.right.right = Node(6)

# root.left.right = Node(5)

# root.left.right.left = Node(6)
# root.left.right.right = Node(7)

print(isFullBinaryTree(root))
