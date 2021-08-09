# O(nlog(N)) time | O(1) space
def twoNumberSum(array, target_sum):
    array.sort()
    start = 0
    end = len(array) - 1

    while start < end:
        start_value = array[start]
        end_value = array[end]
        current_sum = start_value + end_value

        if current_sum == target_sum:
            return [start_value, end_value]
        elif current_sum > target_sum:
            end -= 1
        elif current_sum < target_sum:
            start += 1

    return []


arr = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10

if __name__ == "__main__":
    print(twoNumberSum(arr, target))
