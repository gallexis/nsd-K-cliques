from utils import *
import matrix
import itertools

def get_neighbours(node,graph):
    return graph[node]

def get_clique(k,B,graph):
    A = set()

    while len(B) > 0 and len(A) < k:
        n = B.pop(0)
        A.add(n)
        B = list(set(B).intersection(get_neighbours(n, graph)))
        if k == len(A):
            return {" ".join(sorted(A))} #--> convert {'c','a','b'} to "a b c"

    return []

def get_k_clique(k,graph):
    clique = []

    for node in graph:
        B = set()
        [B.add(n) for n in get_neighbours(node,graph)]
        for subset in itertools.permutations(B, k):
            c = get_clique(k,list(subset),graph)
            clique += c

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

    with open("graph", "r+") as file:
        graph= file.read().splitlines()

        lg = load_graph(graph)
        delete_loop(lg)

        print("Loaded graph:", lg,"\n")

        #Test with predefined cliques
        #test = merge_cliques({"1 2","1 2 3","4 3 1 2","4","2 9"})
        #print("------> Test merged clique: ", test, "\n")


        ### Display a k-clique
        #k = 3
        #clique = get_k_clique(k,lg)

        #print(k,"-clique: ",clique)
        #print("merged clique: ",merge_cliques(clique),"\n")


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
