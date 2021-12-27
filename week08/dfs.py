def dfs(graph: Graph, source: Vertex) -> None:
    source.visited = True
    # Do something
    for vertex in neighbours(source):
        if not vertex.visited:
            dfs(graph, vertex)
