# O(N) time | O(1) space
def isValidSubsequence(array, sequence):
    seqIdx = 0

    for num in array:
        if seqIdx < len(sequence) and num == sequence[seqIdx]:
            seqIdx += 1

    return seqIdx == len(sequence)


arr = [5, 1, 22, 25, 6, -1, 8, 10]
seq = [1, 6, -1, 10]

arr2 = [1, 1, 1, 1, 1]
seq2 = [1, 1, 1]

arr3 = [5, 1, 22, 25, 6, -1, 8, 10]
seq3 = [5, 1, 22, 22, 25, 6, -1, 8, 10]

arr4 = [5, 1, 22, 25, 6, -1, 8, 10]
seq4 = [26]

if __name__ == '__main__':
    print(isValidSubsequence(arr2, seq2))
