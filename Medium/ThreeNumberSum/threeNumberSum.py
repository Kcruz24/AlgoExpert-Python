

def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []

    for idx in range(len(array) - 2):
        curr_num = array[idx]
        left_ptr = idx + 1
        right_ptr = len(array) - 1

        while left_ptr < right_ptr:
            left_num = array[left_ptr]
            right_num = array[right_ptr]

            sum = curr_num + left_num + right_num
            sum_list = [curr_num, left_num, right_num]

            if sum < targetSum:
                left_ptr += 1
            elif sum > targetSum:
                right_ptr -= 1
            else:
                triplets.append(sum_list)
                left_ptr += 1
                right_ptr -= 1

    return triplets
