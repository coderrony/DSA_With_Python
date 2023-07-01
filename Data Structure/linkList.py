
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self) -> None:
        self.head = None

    def nodeLength(self):
        temp = self.head
        if temp is None:
            return 0
        else:
            count = 0
            while temp is not None:
                temp = temp.next
                count += 1
            return count

    def insertPosition(self, index, data):
        if self.nodeLength() < index:
            return "invalid index position"
        elif index == 1:
            self.insertHead(data)
        else:
            new_node = Node(data)
            count = 1
            temp = self.head
            prev = None
            while count != index:
                prev = temp
                temp = temp.next
                count += 1

            prev.next = new_node
            new_node.next = temp

    def insertHead(self, data):
        new_node = Node(data)
        if self.head is Node:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertTail(self, data):
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = Node(data)

    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.data, end="-> ")
            temp = temp.next
        print("None")

    # delete Node

    def deleteHead(self):
        temp = self.head
        self.head = self.head.next
        del temp

    def deleteTail(self):
        temp = self.head
        while (temp.next != None):
            prev = temp
            temp = temp.next
        prev.next = None
        del temp

    def deleteNode(self, position):
        size = self.nodeLength()
        print(size, position)
        if position > size:
            print("position is bigger then size")
        elif size == 1:
            self.deleteHead()
        elif size == position:
            self.deleteTail()
        else:
            count = 1
            temp = self.head

            while count != position:
                prev = temp
                temp = temp.next
                count += 1
            prev.next = temp.next
            # print(temp.data, prev.data)

    def sortList(self):
        current = self.head

        while current.next != None:
            index = current.next
            while index != None:
                if current.data < index.data:
                    current.data, index.data = index.data, current.data
                index = index.next

            current = current.next


head = LinkList()

head.insertHead(0)
head.insertHead(5)
head.insertHead(10)
head.insertHead(15)
head.insertTail(20)
head.insertTail(25)
head.insertPosition(2, 100)
head.insertPosition(1, 200)

# print(head.nodeLength())

# delete Node
# head.printList()
# head.deleteHead()
# head.deleteHead()
# head.deleteTail()
# head.deleteTail()
# head.deleteNode(2)
# head.deleteNode(4)
head.printList()
head.sortList()
head.printList()
