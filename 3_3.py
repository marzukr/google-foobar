# def possibleOperations(fuelAmount):
#     moves = [fuelAmount + 1, fuelAmount - 1]
#     if fuelAmount & 1 == 0:
#         moves.append(fuelAmount / 2)
#     return moves

# def dijkstra(start, dest):
#     unvisited = [start]
#     distances = {start: 0}

#     currentI = 0
#     while len(unvisited) != 0:
#         if unvisited[currentI] != dest:
#             connectedNodes = possibleOperations(unvisited[currentI])
#             currentDist = distances[unvisited[currentI]]
#             for node in connectedNodes:
#                 if node not in distances:
#                     distances[node] = float("inf")
#                     unvisited.append(node)
#                 newDist = currentDist + 1
#                 if newDist < distances[node]:
#                     distances[node] = newDist
            
#             del unvisited[currentI]
#             currentI = 0
#             minDist = distances[unvisited[0]]
#             for i in xrange(0, len(unvisited)):
#                 if distances[unvisited[i]] < minDist:
#                     minDist = distances[unvisited[i]]
#                     currentI = i
#         else:
#             return distances[unvisited[currentI]]
                
def answer(n):
    fuel = long(n)
    return zukAlg(fuel)

def zukAlg(n):
    if n == 1:
        return 0
    elif n & 1 == 0:
        divided = n / 2
        return 1 + zukAlg(divided)
    else:
        maxSteps = 0
        newNum = n
        for i in [1, -1]:
            testNum = n + i
            steps = 1
            while testNum & 1 == 0:
                testNum /= 2
                steps += 1
            if steps > maxSteps or testNum == 1:
                maxSteps = steps
                newNum = testNum
        return maxSteps + zukAlg(newNum)

# 15, 30, 31