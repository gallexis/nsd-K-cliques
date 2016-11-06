### K-clique ###

"""
List = []
# do something to remove doubles (using a set) and convert the list as an ordered string

def Findclique(Size k, Graphe G):
	for n in G:
		A = set(n)
		B = set(neighbours of n)

		makeClique(A,B,K)
		G.remove(n)

def makeClique(A,B,k):

	while not B empty() or k < sizeof(A):
		for n in B:
			A.add(n)
			B.add(B - neighbours(B))

			makeClique(A,B,k)
			#A.remove(n)

	if k == sizeof(A):
		List.append(A)

#arg: list of sets of nodes that represent a clique
def f(c):

	for elt
"""

def get_neighbours(node,graph):
    try:
        return graph[node]
    except:
        return set()

def get_clique(k,A,B,graph):
    global clique

    while len(B) > 0 or k < len(A):
        for n in B:
            A.add(n)
            B.difference( get_neighbours(n, graph) ) # or [B.remove(n) for n in get_neighbours(n, graph)]
            get_clique(k,A,B,graph)
            A.remove(n)

        if k == len(A):
            clique.append( list(A) )

def get_k_clique(k,graph):
    clique = []

    for node in graph:
        A = set()
        B = set()

        A.add(node)
        [B.add(n) for n in get_neighbours(node,graph)]

        get_clique(k,A,B,graph)
        #graph.remove(n)

    return clique

## Fin k-clique ##


def get_nodes_from_edge(edge):
    return edge.split(' ')


def get_nodes_from_graph(graph):
    nodesSet = set()

    for edge in graph:
        nodes = get_nodes_from_edge(edge)
        [nodesSet.add(n) for n in nodes]

    return list(nodesSet)

def size_of_graph(graph):

    nodes = get_nodes_from_graph(graph)
    return len(nodes)


def load_graph(graph):
    nodes = {}

    for edge in graph:
        ns = get_nodes_from_edge(edge)
        n0 = ns[0]

        # if node's degree == 0, empty list
        if len(ns) == 1:
            nodes[n0] = set()

        else:
            n1 = ns[1]
            # if nodes already in dict, append his new neighbour
            if n0 in nodes:
                nodes[n0].add(n1)

            # if node not yet in dict, initialise a new list & add his neighbour
            else:
                nodes[n0] = set(n1)

            if n1 in nodes:
                nodes[n1].add(n0)

            # if node not yet in dict, initialise a new list & add his neighbour
            else:
                nodes[n1] = set(n0)

    return nodes

def delete_loop(loadedGraph):
    for node in loadedGraph:
        if node in loadedGraph[node]:
            loadedGraph[node].remove(node)

    return loadedGraph

if "__main__" == __name__:

    with open("graph", "r+") as file:
        graph= file.read().splitlines()

        lg = load_graph(graph)
        delete_loop(lg)

        print("loaded graph:", lg)
        print("2-clique: ",get_k_clique(2,lg))


