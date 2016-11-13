import matrix

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
    return graph[node]

def get_clique(k,A,B,graph):
    while len(B) > 0 and len(A) < k:
        n = B.pop()
        A.add(n)
        B= B.intersection(get_neighbours(n, graph))

        if k == len(A):
            sub_cliques = get_clique(k,A,B,graph)

            #[" ".join(sorted(A))] --> convert {'b','a','c'} to "a b c"
            return list(set( [" ".join(sorted(A))] + sub_cliques) )

    return []

def get_k_clique(k,graph):
    clique = []

    for node in graph:
        A = set()
        B = set()

        A.add(node)
        [B.add(n) for n in get_neighbours(node,graph)]
        clique += get_clique(k,A,B,graph)

    return clique


def merge_cliques(cliques):
    list_of_sets = []
    final_list_of_sets = []
    clique_list = sorted(cliques , key=str.__len__)

    [list_of_sets.append(set(c.split(' '))) for c in clique_list]

    index = 0
    max_len = len(list_of_sets)
    while index < max_len:
        set1 = list_of_sets[index]

        if is_biggest_set(set1, list_of_sets, index+1, max_len):
            final_list_of_sets.append(" ".join(sorted(set1)))

        index+=1

    return final_list_of_sets

def is_biggest_set(set1, sets, index, max_len):
    while index < max_len:
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

        #Test with predefined cliques
        #test = merge_cliques({"1 2","1 2 3","4 3 1 2","4","2 9"})
        #print("------> Test merged clique: ", test, "\n")


        ### Display a k-clique
        k = 3
        clique = get_k_clique(k,lg)

        print(k,"-clique: ",clique)
        print("merged clique: ",merge_cliques(clique),"\n")

        ### Generate then merge k1 to kn cliques
        k1= 2
        k2= 5
        cliques = []
        print(k1,"to ",k2,"clique:")

        for k in range(k1,k2+1):
            print("Generation of a",k,"clique")
            cliques += get_k_clique(k,lg)

        print("All cliques: ", cliques)

        merged_cliques = merge_cliques(cliques)
        print("Merged cliques: ", merged_cliques)

        overlapMatrix = matrix.createOverlapMatrix(merged_cliques)
        print(matrix.createCommunitiesMatrix(overlapMatrix, 4))