import copy
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
clique = set()

def get_neighbours(node,graph):
    try:
        return graph[node]
    except:
        return set()

def get_clique(k,A,B,graph):
    global clique

    while len(B) > 0 and len(A) < k :
        for n in B:
            A.add(n)
            NewB=copy.deepcopy(B)
            NewB.remove(n)
            NewB=NewB.intersection(get_neighbours(n, graph))
            if k == len(A):
                clique.add(" ".join(sorted(A)))
                return
            if len(NewB) == 0:
                return
            get_clique(k,A,NewB,graph)
            #A.remove(n)



def get_k_clique(k,graph):

    for node in graph:
        A = set()
        B = set()

        A.add(node)
        [B.add(n) for n in get_neighbours(node,graph)]
        get_clique(k,A,B,graph)
        #graph.remove(n)

    return clique


def merge_cliques(cliques):
    clique_list_of_sets = []
    final_clique_list_of_sets = []

    clique_list = sorted(cliques , key=str.__len__)
    [clique_list_of_sets.append(set(c.split(' '))) for c in clique_list]

    for set1 in clique_list_of_sets:
        if is_bigger_set(set1,clique_list_of_sets):
            final_clique_list_of_sets.append(set1)

    return final_clique_list_of_sets

def is_bigger_set(set1,sets):
    for set2 in sets:
        if set1 == set2:
            continue
        elif set1.issubset(set2):
            return False

    return True

def remove_subsets(sets):
    subset = []

    for index,elt in enumerate(sets):
        pass

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
        c =get_k_clique(3,lg)
        print("2-clique: ",c)
        print(merge_cliques(set(["1 2 3","1 2 3","1 2 3 4 5","1 3 5", "3 4 5 6"])))

