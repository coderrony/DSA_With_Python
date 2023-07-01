# Build max heap
def heapify(arr, n, i):  # root element always biggest
    root = i
    left = (i*2) + 1
    right = (i*2) + 2

    if (left < n and arr[left] > arr[root]):
        root = left

    if (right < n and arr[right] > arr[root]):
        root = right

    if (i != root):
        temp = arr[i]
        arr[i] = arr[root]
        arr[root] = temp
        heapify(arr, n, root)


arr = [1, 12, 9, 5, 6, 10]
n = len(arr)
i = int((len(arr) / 2) - 1)

# heapify(arr, n, i)

for i in range(n//2 - 1, -1, -1):
    heapify(arr, n, i)

for i in range(n-1, -1, -1):
    temp = arr[0]  # swap will exchange first large value to the last value
    arr[0] = arr[i]
    arr[i] = temp

    # Heapify root element to get highest element at root again
    heapify(arr, i, 0)

print(arr)
