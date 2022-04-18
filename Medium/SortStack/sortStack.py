# O(N^2) time | O(N) space
def sortStack(stack):
    if len(stack) == 0:
        return stack

    top = stack.pop()

    sortStack(stack)
    insert_sorted_order(stack, top)

    return stack


def insert_sorted_order(stack, value):
    if len(stack) == 0 or stack[-1] <= value:
        stack.append(value)
        return

    top = stack.pop()

    insert_sorted_order(stack, value)

    stack.append(top)


if __name__ == '__main__':
    stack = [-5, 2, -2, 4, 3, 1]

    print(sortStack(stack))
