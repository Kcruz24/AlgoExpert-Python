# O(N) time | O(D) space - where "D" is the innermost depth of the levels of
# the lists
def productSum(array, depth=1):
    sum = 0
    for elem in array:
        if type(elem) is int:
            sum += elem
        else:
            sum += productSum(elem, depth + 1)
    return sum * depth


arr = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]

if __name__ == '__main__':
    print(productSum(arr))
