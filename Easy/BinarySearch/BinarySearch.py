# Iterative approach
# O(log(N)) time | O(1) space
def binarySearch(array, target):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            end = mid - 1
        elif target > array[mid]:
            start = mid + 1

    return - 1


# Recursive approach
# O(log(N)) time | O(log(N)) space
def binarySearchRecursive(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper(array, target, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return binarySearchHelper(array, target, start, mid - 1)
    elif target > array[mid]:
        return binarySearchHelper(array, target, mid + 1, end)


arr = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target_num = 33

if __name__ == '__main__':
    print(binarySearch(arr, target_num))
