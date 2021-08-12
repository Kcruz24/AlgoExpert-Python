def swap(idx_one, idx_two, array):
    array[idx_one], array[idx_two] = array[idx_two], array[idx_one]


# O(N^2) time | O(1) space
def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(j, j - 1, array)
            j -= 1
    return array


arr = [8, 5, 2, 9, 5, 6, 3]

if __name__ == '__main__':
    print(insertion_sort(arr))
