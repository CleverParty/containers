import os,math
import random as r

q = []
distance = []
# default elegant graph format
graph = { "a" : ["c"], 
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }

example_graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}

def generateEdges(graph):
    edgesInner = []
    for node in graph:
        for adjacent in graph[node]:
            edgesInner.append([node,adjacent])
    return edgesInner

def generateWeights(edges):
    weightsInner = []
    for _ in edges:
        weightsInner.append(r.randint(1,10))
    return weightsInner
   
def djik(graph,start):
    distance[start] = 0
    for v in graph:
        if v == start :
            distance[start] = -1
        q.append(distance[v])

def main():
    edges = generateEdges(graph)
    weights = generateWeights(edges)
    print(weights)
    print(edges)

if __name__ == "__main__":
    main()