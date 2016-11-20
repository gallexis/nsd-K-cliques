from utils import *
import matrix
import itertools

def get_neighbours(node,graph):
    return graph[node]

def get_clique(node,k,B,graph):
    A = set()
    A.add(node)
    while len(B) > 0 and len(A) < k:
        n = B.pop(0)
        A.add(n)
        B = list(set(B).intersection(get_neighbours(n, graph)))
        if k == len(A):
            return {" ".join(sorted(A))}

    return []

def get_k_clique(k,graph):
    clique = []

    for node in graph:
        B = set()
        [B.add(n) for n in get_neighbours(node,graph)]
        for subset in itertools.permutations(B, k-1):
            clique += get_clique(node,k,list(subset),graph)

    return clique

def merge_cliques(cliques_set):
    list_of_sets = []
    final_list_of_sets = []
    clique_list = sorted(cliques_set, key=str.__len__)

    [list_of_sets.append(set(c.split(' '))) for c in clique_list]

    index = 0
    max_len = len(list_of_sets)
    while index < max_len:
        set1 = list_of_sets[index]

        if is_biggest_subset(set1, list_of_sets, index+1, max_len):
            final_list_of_sets.append(sorted(set1))

        index+=1

    return final_list_of_sets

def is_biggest_subset(set1, sets, index, max_len):
    while index < max_len:
        if set1.issubset(sets[index]):
            return False

        index +=1

    return True


if "__main__" == __name__:

    with open("graph3", "r+") as file:
        graph= file.read().splitlines()

        lg = load_graph(graph)
        delete_loop(lg)

        #print("Loaded graph:", lg,"\n")

        #Test with predefined cliques
        #test = merge_cliques({"1 2","1 2 3","4 3 1 2","4","2 9"})
        #print("------> Test merged clique: ", test, "\n")


        ### Display a k-clique
        """
        k = 4
        clique = get_k_clique(k,lg)

        print(k,"-clique: ",clique)
        print("merged clique: ",merge_cliques(clique),"\n")
        """

        ### Generate then merge k1 to kn cliques
        cliques = []
        k1 = 2
        k2 = get_max_degree_nodes(lg)+1

        while True:
            print("Generation of a",k1,"clique")
            c= get_k_clique(k1,lg)
            if c == []:
                break
            k1 += 1
            cliques += c

        #print("All cliques: ", cliques)
        merged_cliques = merge_cliques(cliques)

        #print("Merged cliques: ", merged_cliques)

        overlapMatrix = matrix.createOverlapMatrix(merged_cliques)
        print(overlapMatrix)
        print(matrix.createCommunitiesMatrix(overlapMatrix,4 ))
