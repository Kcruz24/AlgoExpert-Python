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


arr = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target_num = 33

if __name__ == '__main__':
    print(binarySearch(arr, target_num))
