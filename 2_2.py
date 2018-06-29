def convToTuple(coord):
    return (coord % 8, coord // 8 * -1)

def convToPos(coord):
    return -8 * coord[1] + coord[0]

def withinBounds(coord):
    return coord[0] >= 0 and coord[0] <= 7 and coord[1] <= 0 and coord[1] >= -7

def possibleMoves(coord):
    moves = []
    for i in [1, -1]:
        for j in [2, -2]:
            moves.append((coord[0] + i, coord[1] + j))
            moves.append((coord[0] + j, coord[1] + i))
    moves = [move for move in moves if withinBounds(move)]
    return moves

def dijkstra(start, dest):
    unvisited = []
    distances = {start: 0}
    for i in xrange(0, 64):
        tI = convToTuple(i)
        unvisited.append(tI)
        if i != convToPos(start):
            distances[tI] = float("inf")

    currentNode = start
    while len(unvisited) != 0:
        if currentNode != dest:
            connectedNodes = possibleMoves(currentNode)
            currentDist = distances[currentNode]
            for node in connectedNodes:
                newDist = currentDist + 1
                if newDist < distances[node]:
                    distances[node] = newDist
            
            unvisited.remove(currentNode)
            currentNode = unvisited[0]
            minDist = distances[unvisited[0]]
            for node in unvisited:
                if distances[node] < minDist:
                    minDist = distances[node]
                    currentNode = node
        else:
            return distances[currentNode]
                
def answer(src, dest):
    return dijkstra(convToTuple(src), convToTuple(dest))