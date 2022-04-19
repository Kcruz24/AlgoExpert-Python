# Brute Force
# O(N^2) time | O(N^2) space
def sameBsts(arr_one, arr_two):
    if len(arr_one) == 0 and len(arr_two) == 0:
        return True

    if arr_one[0] != arr_two[0] or len(arr_one) != len(arr_two):
        return False

    left_tree_one = []
    left_tree_two = []
    for val in arr_one[1:]:
        if val < arr_one[0]:
            left_tree_one.append(val)
        else:
            right_tree_one.append(val)

    right_tree_one = []
    right_tree_two = []
    for val in arr_two[1:]:
        if val < arr_two[0]:
            left_tree_two.append(val)
        else:
            right_tree_two.append(val)

    return sameBsts(left_tree_one, left_tree_two) and sameBsts(right_tree_one, right_tree_two)


if __name__ == '__main__':
    one = [10, 15, 8, 12, 94, 81, 5, 2, 11]
    two = [10, 8, 5, 15, 2, 12, 11, 94, 81]

    print(sameBsts(one, two))
