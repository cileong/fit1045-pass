from stack import Stack

def matching_parentheses(s: str) -> bool:
    stack = Stack()
    for char in s:
        if char == '(':
            stack.push('(')
        elif char == ')':
            if stack.is_empty() or not stack.pop() == '(':
                return False
    return True

if __name__ == '__main__':
    s = '()()(())())'
    print(matching_parentheses(s))
    