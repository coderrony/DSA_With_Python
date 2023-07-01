

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def perOrder(root):
    if root:
        print(root.data, end=" ")
        perOrder(root.left)
        perOrder(root.right)


def deepCount(root):
    count = 0
    while root is not None:
        count += 1
        root = root.left
    return count


def checkPerfect(root,  deep, level=0):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return deep == level+1

    if root.left is None or root.right is None:
        return False

    return checkPerfect(root.left, deep, level+1) and checkPerfect(root.right, deep, level+1)


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

# perOrder(root)

# print(deepCount(root))

d = deepCount(root)
print(d)

print(checkPerfect(root, d, 0))
