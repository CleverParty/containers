import random
import os, math
visited = []
# example graph :
graph = { "a" : ["c"], 
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }

def search(value):
    if(value == graph[value]):
        print(f'here')
    # if(value in graph):
    #     print(f'logix')
    elif(value not in visited):
        print(f'already here')
        visited.append(value)
        for current in graph[value]:
            search(current)


def main():
    search("c")

if __name__ == "__main__":
    main()
    print(visited)