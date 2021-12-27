from typing import Generic, TypeVar

T = TypeVar('T')

class Queue:

    def __init__(self) -> None:
        self.arr = []

    def enqueue(self, item: T) -> None:
        self.arr.append(item)

    def dequeue(self) -> T:
        return self.arr.pop(0)

    def is_empty(self) -> bool:
        return len(self) == 0

    def __len__(self) -> int:
        return len(self.arr)

    def __str__(self) -> str:
        return str(self.arr)

if __name__ == '__main__':
    queue = Queue()
    for i in range(10):
        queue.enqueue(i)
    for _ in range(5):
        item = queue.dequeue()
        print(item)
        