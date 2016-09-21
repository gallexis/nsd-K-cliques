
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


# Exercice 5
"""
Yes it is necessary to store the graph in memory, otherwise we would have to browse the file from the beginning to the end
of the file to look for all neigbours of one node, and compute that task for each nodes.
"""
def get_zero_degree_nodes(loadedGraph):
    zero = []

    for node, neighbours in loadedGraph.items():
        if len(neighbours) == 0:
            zero.append(node)

    return len(zero)

def get_density_nodes(loadedGraph):
    pass

def get_average_degree_nodes(loadedGraph):
    pass

def get_min_degree_nodes(loadedGraph):
    return len( min(loadedGraph.values()) )

def get_max_degree_nodes(loadedGraph):
    return len( max(loadedGraph.values()) )


if "__main__" == __name__:

    with open("graph2", "r+") as file:
        graph= file.read().splitlines()

        print("Exercise n°2, size of graph: ", size_of_graph(graph))
        print("Exercise n°3, degree of each nodes:", nodes_degrees(graph))


        ld = load_graph(graph)

        print("\nExercise n°5:")
        print("\tNumber of nodes of degree 0: ",get_zero_degree_nodes(ld))
        print("\tDensity of the graph: ")
        print("\tAverage degre of the graph: ")
        print("\tMinimum degree of the graph: ",get_min_degree_nodes(ld))
        print("\tMaximum degree of the graph: ",get_max_degree_nodes(ld))
