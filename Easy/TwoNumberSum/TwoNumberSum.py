# O(N) time | O(N) space
def twoNumberSum(array, targetSum):
    distinct_nums = set()

    for num in array:
        potential_match = targetSum - num
        if num not in distinct_nums:
            distinct_nums.add(potential_match)
        else:
            return [num, potential_match]

    return []


# O(Nlog(N)) time | O(1) space
def twoNumberSum(array, targetSum):
    array.sort()

    start = 0
    end  = len(array) - 1
    while start < end:
        if array[start] + array[end] < targetSum:
            start += 1
        elif array[start] + array[end] > targetSum:
            end -= 1
        else:
            return [array[start], array[end]]
    return []


arr = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10

if __name__ == "__main__":
    print(twoNumberSum(arr, target))
