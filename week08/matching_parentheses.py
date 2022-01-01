from stack import Stack

def matching_parentheses(s: str) -> bool:
    stack = Stack()
    for char in s:
        if char == '(':
            stack.push('(')
        elif char == ')':
            if stack.is_empty() or not stack.pop() == '(':
                return False
            
    # If the stack is not empty,
    # that means there are some unmatched opening parentheses
    return stack.is_empty()

if __name__ == '__main__':
    s = '()()(())())'
    print(matching_parentheses(s))
    
