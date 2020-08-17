import os,math
import random as r

# input default elegant graph format
graph = { "a" : ["c"], 
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
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
   

def main():
    edges = generateEdges(graph)
    weights = generateWeights(edges)
    print(weights)
    print(edges)

if __name__ == "__main__":
    main()