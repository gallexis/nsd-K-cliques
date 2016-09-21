
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
        n0 = nodes[0]

        if len(nodes) == 1:
            nodesDegrees[n0] = 0

        elif n0 in nodesDegrees:
            nodesDegrees[n0] += 1

        else:
            nodesDegrees[n0] = 1

    return nodesDegrees

# Exercice 4
def load_graph(graph):
    nodes = {}

    for edge in graph:
        ns = get_nodes_from_edge(edge)
        n0 = ns[0]

        # if node's degree == 0, empty list
        if len(ns) == 1:
            nodes[n0] = []

        # if nodes already in disct, append his new neighbour
        elif n0 in nodes:
            nodes[n0].append(ns[1])

        # if node not yet in dict, initialise a new list & add his neighbour
        else:
            nodes[n0] = [ns[1]]

    return nodes









if "__main__" == __name__:

    with open("graph", "r+") as file:
        graph= file.read().splitlines()

        print("Exercise n°2, size of graph: ", size_of_graph(graph))
        print("Exercise n°3, degree of each nodes:", nodes_degrees(graph))

        a = load_graph(graph)
        print(a)