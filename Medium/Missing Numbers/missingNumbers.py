# O(N) Time | O(N) Space
def missingNumbers(nums):
    numSet = set(nums)
    missing = []
    for i in range(1, len(nums) + 3):
        if i not in numSet:
            missing.append(i)

    return missing


if __name__ == '__main__':
    test = [1, 4, 3]
    print(missingNumbers(test))