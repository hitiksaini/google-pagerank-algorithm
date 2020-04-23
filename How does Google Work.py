#!/usr/bin/env python
# coding: utf-8

# In[10]:


import networkx as nx
import random
import matplotlib.pyplot as plt
import operator
G=nx.gnp_random_graph(10,0.5,directed=True)  #.5 for edge creation prob.
nx.draw(G,with_labels= True)
plt.show()
x=random.choice([i for i in range(G.number_of_nodes())])  #random source node
dict_counter={}
for i in range(G.number_of_nodes()):
    dict_counter[i]=0
dict_counter[x]=dict_counter[x]+1
for i in range(1000000):    #we iterate here and wait for convergence of the points distributed
    list_n= list(G.neighbors(x))
    if(len(list_n)==0):   #if x is sink(no neighbor)
        x=random.choice([i for i in range(G.number_of_nodes())])
        dict_counter[x]=dict_counter[x]+1
    else:
        x=random.choice(list_n)
        dict_counter[x]=dict_counter[x]+1
p=nx.pagerank(G)
sorted_p= sorted(p.items(), key= operator.itemgetter(1))
sorted_rw= sorted(dict_counter.items(), key= operator.itemgetter(1))
print(sorted_p)
print(sorted_rw)
#we now match if the order comes in same as like 5-> 3-> ...  otherwise increase the iterations


# In[25]:


import networkx as nx
import random
import matplotlib.pyplot as plt

def add_edges():
    nodes= list(G.nodes())
    for s in nodes:
        for t in nodes:
            if s != t:
                r=random.random()
                if r<0.5:
                    G.add_edge(s,t)
    return G

def ap(G):
    nodes= list(G.nodes())
    p=[]
    for each in nodes:
        p.append(100)    #we assign point to each node 
    return p

def distribute_points(G, points):
    nodes= list(G.nodes())
    new_points=[]
    for i in range(len(nodes)):
        new_points.append(0)
    for n in nodes:
        out=list(G.out_edges(n))
        if(len(out)==0):
            new_points=new_points[n]+points[n]
        else:
            share= points[n]/len(out)
            for(src, tgt) in out:
                new_points[tgt]= new_points[tgt]+share
    return new_points
    
def keep_distributing(points, G):
    while(1):
        new_points= distribute_points(G, points)
        print(new_points)
        points= new_points
        stop=input("press n to stop or any other key to continue")
        if stop=="n":
            break
        else:
            continue
        return new_points
    
def rank_by_points(final_points):
    d={}
    for i in range(len(points)):
        d[i]= points[i]
        print(sorted(d.items(), key=lambda f:f[1]))
    
G=nx.DiGraph()  # a directed graph
G.add_nodes_from([i for i in range(10)])
G=add_edges()
nx.draw(G,with_labels= True)
plt.show()
#assign points
points= ap(G)
#distribute // convergence
final_points= keep_distributing(points, G)
#rank by points
rank_by_points(final_points)
print("now compare it")
result= nx.pagerank(G)
print(sorted(result.items(), key=lambda f:f[1]))


# In[ ]:




