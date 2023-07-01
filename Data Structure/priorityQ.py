
def heapify(arr, size, root):
    large = root
    left = (root * 2) + 1
    right = (root * 2) + 2

    if left < size and arr[left] > arr[large]:
        large = left

    if right < size and arr[right] > arr[large]:
        large = right

    if root != large:
        arr[large], arr[root] = arr[root], arr[large]
        heapify(arr, size, large)


def insert(arr, value):
    if len(arr) == 0:
        arr.append(value)
    else:
        arr.append(value)
        for i in range((len(arr) // 2)-1, -1, -1):
            heapify(arr, len(arr), i)


def deleteNode(arr, num):
    i = 0
    for i in range(0, len(arr)):
        if arr[i] == num:
            break

    arr[i], arr[len(arr)-1] = arr[len(arr)-1], arr[i]
    arr.pop()
    for i in range((len(arr) // 2)-1, -1, -1):
        heapify(arr, len(arr), i)


arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print("Max-Heap array: " + str(arr))

deleteNode(arr, 9)
deleteNode(arr, 5)
print("After deleting an element: " + str(arr))
