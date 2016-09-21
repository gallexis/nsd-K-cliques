
def get_nodes_from_edge(edge):
    nodes = edge.split(' ')
    return nodes[0], nodes[1]


def get_nodes_from_graph(graph):
    nodes = set()

    for edge in graph:
        n1,n2 = get_nodes_from_edge(edge)
        nodes.add(n1)
        nodes.add(n2)

    return list(nodes)

#Exercise 2
def size_of_graph(graph):
    nodes = get_nodes_from_graph(graph)
    return len(nodes)

#Exercise 3
def nodes_degrees(graph):
    nodesDegrees = {}

    for edge in graph:
        n1,n2 = get_nodes_from_edge(edge)

        if n1 in nodesDegrees:
            nodesDegrees[n1] += 1
        else:
            nodesDegrees[n1] = 1

    return nodesDegrees


if "__main__" == __name__:

    with open("graph", "r+") as file:
        graph= file.read().splitlines()

        print("Exercise n°2, size of graph: ", size_of_graph(graph))
        print("Exercise n°3, degree of each nodes:", nodes_degrees(graph))