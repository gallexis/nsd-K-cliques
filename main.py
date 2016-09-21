
def get_nodes_from_edge(edge):
    return edge.split(' ')


def get_nodes_from_graph(graph):
    nodesSet = set()

    for edge in graph:
        nodes = get_nodes_from_edge(edge)
        [nodesSet.add(n) for n in nodes]

    return list(nodesSet)

#Exercise 2
def size_of_graph(graph):
    nodes = get_nodes_from_graph(graph)
    return len(nodes)

#Exercise 3
def nodes_degrees(graph):
    nodesDegrees = {}

    for edge in graph:
        nodes = get_nodes_from_edge(edge)
        n1 = nodes[0]

        if len(nodes) == 1:
            nodesDegrees[n1] = 0

        elif n1 in nodesDegrees:
            nodesDegrees[n1] += 1

        else:
            nodesDegrees[n1] = 1

    return nodesDegrees


if "__main__" == __name__:

    with open("graph", "r+") as file:
        graph= file.read().splitlines()

        print("Exercise n°2, size of graph: ", size_of_graph(graph))
        print("Exercise n°3, degree of each nodes:", nodes_degrees(graph))