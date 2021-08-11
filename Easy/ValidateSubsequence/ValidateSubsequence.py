# O(N) time | O(1) space
def isValidSubsequence(array, sequence):
    if len(sequence) > len(array) or sequence[0] not in array:
        return False

    if all(elem == sequence[0] for elem in array):
        return True

    current_idx = 0

    for i in range(1, len(sequence)):
        if sequence[i] in array:
            array_idx = array.index(sequence[i])
            if array_idx > current_idx:
                current_idx = array_idx
            else:
                return False
        else:
            return False
    return True


# Algo Expert Solution
# O(N) time | O(1) space
def isValidSubsequence2(array, sequence):
    arr_idx = 0
    seq_idx = 0

    while arr_idx < len(array) and seq_idx < len(sequence):
        if sequence[seq_idx] == array[arr_idx]:
            seq_idx += 1
        arr_idx += 1

    return seq_idx == len(sequence)


arr = [5, 1, 22, 25, 6, -1, 8, 10]
arr2 = [1, 1, 1, 1, 1]
seq = [1, 6, -1, 10]
seq2 = [1, 1, 1]
arr3 = [5, 1, 22, 25, 6, -1, 8, 10]
seq3 = [5, 1, 22, 22, 25, 6, -1, 8, 10]

arr4 = [5, 1, 22, 25, 6, -1, 8, 10]
seq4 = [26]

if __name__ == '__main__':
    print(isValidSubsequence2(arr2, seq2))
