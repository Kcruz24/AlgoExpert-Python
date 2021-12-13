# O(N) time | O(1) space
def kadanesAlgorithm(array):
    max_sub_array_sum = 0
    running_sum = 0

    for num in array:
        running_sum += num
        if running_sum < num:
            running_sum = 0 
        if num < 0 and running_sum <= 0:
            running_sum = 0
        elif num < 0:
            last_sum_before_negative = running_sum + abs(num)
            if last_sum_before_negative > max_sub_array_sum:
                max_sub_array_sum = last_sum_before_negative

    if running_sum > max_sub_array_sum:
        max_sub_array_sum = running_sum

    return max_sub_array_sum


# Algo Expert solution
# O(N) time | O(1) space
def kadanesAlgorithm2(array):
    max_ending_here = array[0]
    max_so_far = array[0]

    for num in array[1:]:
        max_ending_here = max(max_ending_here + num, num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


if __name__ == '__main__':
    array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
    array2 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

    print(kadanesAlgorithm(array))
    print(kadanesAlgorithm2(array2))