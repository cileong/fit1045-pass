from queue import Queue

def bfs(graph: Graph, source: Vertex) -> None:
    queue = Queue()
    queue.enqueue(source)
    source.visited = True

    while not queue.is_empty():
        current = queue.dequeue()

        # Usually you do something here
        print(current)

        current.visited = True
        
        for vertex in neighbours_of(current):
            if not vertex.visited:
                queue.enqueue(vertex)