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

def get_k_clique(k,graph):

    for node in graph:
        A = set()
        B = set()

        A.add(node)
        [B.add(n) for n in get_neighbours(node,graph)]
        get_clique(k,A,B,graph)

    return clique


def merge_cliques(cliques):
    clique_list_of_sets = []
    final_clique_list_of_sets = []
    clique_list = sorted(cliques , key=str.__len__)

    [clique_list_of_sets.append(set(c.split(' '))) for c in clique_list]

    index = 0
    max_len = len(clique_list_of_sets)
    while index < max_len-1:
        set1 = clique_list_of_sets[index]

        if is_biggest_subset(set1, clique_list_of_sets, index+1,max_len):
            final_clique_list_of_sets.append(" ".join(sorted(set1)))

        index+=1

    # The last one is not in the previous iteration, and must always be added in the list
    # (as long as the list is sorted)
    final_clique_list_of_sets.append(" ".join(sorted(clique_list_of_sets[max_len-1])))

    return final_clique_list_of_sets

def is_biggest_subset(set1, sets, index,max_len):
    while index < max_len - 1:
        if set1.issubset(sets[index]):
            return False
        index +=1

    return True

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

        print("Loaded graph:", lg,"\n")

        ### Display a k-clique
        k = 2
        clique = get_k_clique(k,lg)

        print(k,"-clique: ",clique)
        print("merged clique: ",merge_cliques(clique),"\n")

        ### Generate then merge k1 to kn cliques
        k1= 2
        k2= 4
        cliques = []
        print(k1,"to ",k2,"clique:")

        for k in range(k1,k2+1):
            cliques += get_k_clique(k,lg)

        print("all cliques: ", cliques)

        merged_cliques = merge_cliques(cliques)
        print("merged cliques: ", merged_cliques)