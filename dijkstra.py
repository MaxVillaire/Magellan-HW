#!/bin/python3

import sys
import math

# helper method for shortest distance
def shortestDist(d,  vis, n):
    #init min
    minimum, min_ind = [math.inf,0]
    
    #check each of the distance values, find min
    for v in range(n):
        if d[v] < minimum and vis[v] == False:
            # print('Found min %d'%v)
            minimum = d[v]
            min_ind = v
    #return the index, not value
    return min_ind
    



# t is the number of test cases
t = int(input().strip())

for a0 in range(t):   
    
    # n is number of nodes
    # m is number of edges
    n,m = input().strip().split(' ')
    n,m = [int(n),int(m)]

    # store the graph in adjacency matrix
    graph = [ [ math.inf for i in range(n) ] for _ in range(n)]
    
    # For each edge
    for a1 in range(m):
        # read the edge
        x,y,r = input().strip().split(' ')
        x,y,r = [int(x)-1,int(y)-1,int(r)]
        
        # Set it both ways b/c undirected graph
        if graph[x][y] > r:
            graph[x][y] = r
        if graph[y][x] > r:
            graph[y][x] = r
    # print(graph)
    
    # dist will hold the distance to each node, initialize to inf
    dist = [math.inf] * n
    visited = [False] * n
    
    # s is the starting node
    s = int(input().strip())
    
    # Set the initial conditions
    dist[s-1] = 0

    for k in range(n):
        
        # Find the shortest distance node that hasn't been visited
        u = shortestDist(dist,visited,n)
        # print(u)

        # We have now visited this node
        visited[u] = True
        
        for v in range(n):
            if not graph[u][v] == math.inf and visited[v] == False and dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]
        
    # format the results and print
    # print(dist)
    ret = [x if not x == math.inf else -1 for x in dist]
    # print(ret)
    del ret[s-1]
    print(*ret)
