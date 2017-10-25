# -*- coding: utf-8 -*-
"""
Created on Tue Aug 09 13:38:33 2016

@author: Xiaoqian Xie

ELEN90061 Workshop 3_ 709716-850965 of session Thu-9
"""
import sys
import networkx as nx
import matplotlib.pyplot as plt

Inf = sys.maxsize # Infinity 

# Create the graph
G = nx.Graph()
G.add_nodes_from(['u', 'v', 'x', 'w', 'y', 'z'])
G.add_weighted_edges_from([('u', 'v', 2), ('u', 'w', 5), ('u', 'x', 1), ('x', 'v', 2),
                           ('x', 'w', 3), ('x', 'y', 1), ('v', 'w', 3), ('y', 'w', 1),
                           ('y', 'z', 2), ('w', 'z', 5)])

# get labels and set positions
Glabels = nx.get_edge_attributes(G, 'weight')
pos = {'u': [0, 1], 'v': [1, 2], 'x': [1, 0], 'y': [2, 0], 'w': [2, 2], 'z': [3, 1]}

# Draw the graph
nx.draw(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=Glabels, font_weight='bold')



# c(m,n) calulate the distance between m,n
def c(graphy,m,n):
    E = graphy.edges()
    if (m,n) in E or (n,m) in E:
        return graphy[m][n]['weight']
    elif m == n:
        return 0
    else:
        return Inf

# function is used to find the nearest node of node S
def findminedge(G,S,sub):
    Minlength = Inf 
    Minnode = S
    for i in range(len(sub)):
        if Minlength > c(G, S,sub[i]) and c(G, S,sub[i]) != 0:
            Minlength = c(G, S,sub[i])
            Minnode = sub[i]
    return Minnode

def mydijkstra(inputG,source):
    # Initialization
    N_ = [] # N' set of nodes whose least cost path definitively known
    D = {} # dictionary of current value of cost path from source to destination
    P = {} # dictionary of predecessor node along path 
    N_.append(source) # add source node to N'
    E = inputG.edges()
    N = inputG.nodes()
    # Initialization of D(n)
    for i in range(len(N)):
        D[N[i]] = c(inputG,N_[0],N[i])
        
    # Initialization of p(n) 
    for i in range(len(N)):
        if (source, N[i]) in E or (N[i],source) in E:
            P[N[i]] = source  
    # set the predecessor of source is itself        
    P[source] = source
       
 
    #Main loop
    while len(N_) != len(N)-1: #loop condition 
        
        sub = list(set(N) - set(N_)) # N - N_    
        minnode = findminedge(inputG, N_[-1], sub)

        #update D(n)
        for i in range(len(sub)):
            if D[sub[i]] > D[minnode] + c(inputG,minnode,sub[i]):
                D[sub[i]] = D[minnode] + c(inputG,minnode,sub[i])
                P[sub[i]] = minnode
        N_.append(minnode)
    return D,P

# shortest path of every other node except source node
def shortestpathh(G,sourcenode,P):
    listpath = {} # A dictionary of shortest path
    for i in range(len(G.nodes())):
        N = G.nodes()
        path = []
        end = N[i]
        while 1:
            path.insert(0,end)
            if sourcenode == end:# if find the source node, then jump out of the loop
                break
            end = P.get(end)
        listpath[N[i]] = path 
        
    return listpath

 
# set source node      
sourcenode = 'w'
D,P = mydijkstra(G, sourcenode)

 # print output of mydijkstra() 
print('My dijskstra:\n')  
print(D)
print(shortestpathh(G,sourcenode,P),'\n')                
# For comparision
print('Networkx:\n')
Length,Path = nx.single_source_dijkstra(G,sourcenode)
print(Length) 
print(Path,'\n')




##############################################################################
#Bonus Question

#Graph 1
G1 = nx.Graph()
G1.add_nodes_from(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
G1.add_weighted_edges_from([('a', 'b', 2), ('c', 'd', 7), ('e', 'f', 9), ('g', 'h', 2),
                           ('a', 'd', 3), ('c', 'b', 4), ('e', 'g', 3), ('h', 'd', 1),
                           ('d', 'f', 2), ('g', 'b', 5)])
# set source node      
sourcenode1 = 'b'
D1,P1 = mydijkstra(G1, sourcenode1)

 # print output of mydijkstra()   
print('Test 1') 
print('My dijskstra:\n') 
print(D1)
print(shortestpathh(G1,sourcenode1,P1),'\n')                
# For comparision
print('Networkx:\n')
Length1,Path1 = nx.single_source_dijkstra(G1,sourcenode1)
print(Length1) 
print(Path1,'\n')


#Graph 2
G2 = nx.Graph()
G2.add_nodes_from(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
G2.add_weighted_edges_from([('a', 'b', 3), ('c', 'd', 30), ('e', 'f', 10), ('g', 'h', 60),
                           ('a', 'd', 12), ('c', 'b', 4), ('e', 'g', 30), ('h', 'd', 18),
                           ('d', 'f', 4), ('g', 'b', 5)])
# set source node      
sourcenode2 = 'c'
D2,P2 = mydijkstra(G2, sourcenode2)

 # print output of mydijkstra()  
print('Test 2') 
print('My dijskstra:\n') 
print(D2)
print(shortestpathh(G2,sourcenode2,P2),'\n')                
# For comparision
print('Networkx:\n')
Length2,Path2 = nx.single_source_dijkstra(G2,sourcenode2)
print(Length2) 
print(Path2,'\n')

    









    

