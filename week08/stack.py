from typing import Generic, TypeVar, List

T = TypeVar('T')

class Stack(Generic[T]):

    def __init__(self) -> None:
        self.arr = []
    
    def push(self, item: T) -> None:
        self.arr.append(item)

    def pop(self) -> T:
        if self.is_empty():
            raise Exception('Cannot pop from an empty stack.')
        return self.arr.pop()

    def peek(self) -> T:
        if self.is_empty():
            raise Exception('Cannot peek at an empty stack.')
        return self.arr[-1]

    def is_empty(self) -> bool:
        return len(self) == 0

    def to_list(self) -> List[T]:
        return self.arr

    def __len__(self) -> int:
        return len(self.arr)

    def __str__(self) -> str:
        return str(list(reversed(self.arr)))

if __name__ == '__main__':
    stack = Stack()
    for i in range(10):
        stack.push(i)
    for _ in range(5):
        item = stack.pop()
        print(item)
