# O(N)^2 time | O(N) space
def nextGreaterElement(array):
    greatest_elements = []

    for idx_one in range(len(array)):
        idx_two = (idx_one + 1) % len(array)

        while idx_two != idx_one:
            if array[idx_two] > array[idx_one]:
                greatest_elements.append(array[idx_two])
                break
            else:
                idx_two = (idx_two + 1) % len(array)

        if idx_two == idx_one:
            greatest_elements.append(-1)

    return greatest_elements


if __name__ == '__main__':
    array = [2, 5, -3, -4, 6, 7, 2]

    print(nextGreaterElement(array))