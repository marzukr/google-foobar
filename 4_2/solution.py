def equalizes(a,b):
    if (a+b) & 1 == 0:
        multiple = a+b
        # for i in xrange(0,16):
        #     if multiple & 1 == 0:
        #         multiple /= 2
        #     else:
        #         break
        while multiple & 1 == 0:
            multiple /= 2
        # test = multiple
        return a % multiple == 0
        # while test < a+b:
        #     if test == a or test == b:
        #         return True
        #     test += multiple
    return False

def genGraph(banana_list):
    connections = {}
    for i in xrange(len(banana_list)):
        connections[i] = None
    matches = {}
    for i in xrange(len(banana_list)):
        iMatches = []
        for j in xrange(len(banana_list)):
            if not equalizes(banana_list[i], banana_list[j]):
                iMatches.append(j)
        matches[i] = iMatches
    for i in connections:
        if connections[i] == None:
            for j in connections:
                if connections[j] == None and j in matches[i]:
                    connections[i] = j
                    connections[j] = i
                    break
    return {"pairs": connections, "list": banana_list, "matches": matches}

# def genGraph(banana_list):
#     connections = {}
#     for i in xrange(len(banana_list)):
#         connections[i] = None
#     for i in connections:
#         if connections[i] == None:
#             for j in connections:
#                 if connections[j] == None and not equalizes(banana_list[i], banana_list[j]):
#                     connections[i] = j
#                     connections[j] = i
#                     break
#     return {"pairs": connections, "list": banana_list}

# def genGraph2(banana_list):
#     connections = {}
#     for i in xrange(len(banana_list)):
#         if i in connections:
#             continue
#         for j in xrange(len(banana_list)):
#             if j in connections:
#                 continue
#             elif not equalizes(banana_list[i], banana_list[j]):
#                 connections[i] = j
#                 connections[j] = i
#                 break
#         else:
#             connections[i] = None
#     return {"pairs": connections, "list": banana_list}

def augment(banana_graph):
    for node in banana_graph["pairs"]:
        if banana_graph["pairs"][node] == None:
            for node2 in banana_graph["pairs"]:
                if banana_graph["pairs"][node2] != None and not equalizes(banana_graph["list"][node], banana_graph["list"][node2]):
                    for node3 in banana_graph["pairs"]:
                        if banana_graph["pairs"][node3] == None and node != node3 and not equalizes(banana_graph["list"][banana_graph["pairs"][node2]], banana_graph["list"][node3]):
                            connectNode2 = banana_graph["pairs"][node2]
                            banana_graph["pairs"][node] = node2
                            banana_graph["pairs"][node2] = node
                            banana_graph["pairs"][node3] = connectNode2
                            banana_graph["pairs"][connectNode2] = node3
                            # return [(node,node2), (node3,banana_graph["pairs"][node2])]
                            # print "augment"
                            return True
    return False

def blossom(banana_graph):
    while augment(banana_graph): 
        None == None
    return banana_graph

def answer(banana_list):
    maximized = blossom(genGraph(banana_list))
    guarding = 0
    for node in maximized["pairs"]:
        if maximized["pairs"][node] == None:
            guarding += 1
    return guarding

# g = [1,1,1,4,5,3,1,1,1,4,5,3,1,1,1,4,5,3,1,1,1,4,5,3,1,1,1,4,5,3,1,1,1,4,5,3,1,1,1,4,5,3,1,1,1,4,5,3,1,1,1,4,5,3,1,1,1,4,5,3,1,1,1,4,5,3,1,1,1,4,5,3,1,1,1,4,5,3,1,1,1,4,5,3,1,1,1,4,5,3,1,1,1,4,5,3,1,1,1,4,5,3,1,1,1,4,5,3,1,1,1,4,5,3,1,1,1,4,5,3,1,1,1,4,5,3,1,1,1,4,5,3,1,1,1,4,5,3,1,1,1,4,5,3,1,1,1,4,5,3,1,1,1,4,5,3,1,1,1,4,5,3,1,1,1,4,5,3,1,1,1,4,5,3,1,1,1,4,5,3,1,1,1,4,5,3,1,1,1,4,5,3]
# print genGraph(g) == genGraph2(g)