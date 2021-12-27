from stack import Stack

def stack_sort(stack: Stack):
    aux_stack = Stack()
    while not stack.is_empty():
        top_item = stack.pop()
        while not aux_stack.is_empty() and aux_stack.peek() > top_item:
            item = aux_stack.pop()
            stack.push(item)
        aux_stack.push(top_item)
    return aux_stack


if __name__ == '__main__':
    stack = Stack()
    stack.push(4)
    stack.push(7)
    stack.push(9)
    stack.push(2)
    stack.push(8)

    print(stack)

    sorted_stack = stack_sort(stack)
    print(sorted_stack.arr)
