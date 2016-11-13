
# optimize comparison. Can be done by traingular part
def createOverlapMatrix(cliqueList):
    overlapMatrix = [[0 for _ in range(len(cliqueList))] for _ in range(len(cliqueList))]
    cliquePos = 0
    for clique in cliqueList:
        compCliquePos = 0
        for compClique in cliqueList:
            overlapMatrix[cliquePos][compCliquePos] = len(set(clique).intersection(compClique))
            compCliquePos = compCliquePos + 1
        cliquePos = cliquePos + 1
    # print (overlapMatrix)
    return overlapMatrix

def createCommunitiesMatrix(overlapMatrix, k):
    communititesMatrix = [[0 for _ in range(len(overlapMatrix))] for _ in range(len(overlapMatrix))]
    linePos = 0
    for line in overlapMatrix:
        columnPos = 0
        for node in line:
            if linePos == columnPos:
                if node >= k:
                    communititesMatrix[linePos][columnPos] = 1
            else:
                if node >= k - 1:
                    communititesMatrix[linePos][columnPos] = 1
            columnPos = columnPos + 1
        linePos = linePos + 1
    # print (communititesMatrix)
    return communititesMatrix


if __name__ == "__main__":
    cliqueList = [['d', 'e', 'h', 'i', 'j'], ['d', 'e', 'g', 'h'], ['b', 'd', 'e'], ['b', 'e', 'f'],
                  ['c', 'd', 'i', 'j'], ['a', 'b', 'c', 'd']]
    overlapMatrix = createOverlapMatrix(cliqueList)
    print(createCommunitiesMatrix(overlapMatrix, 4))

