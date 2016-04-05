#!/usr/bin/env python

__author__ = "CS381 John Advanced Programming"

time = 1
a = {} #ancestor
c = {} #color
d = {} #discovered time
f = {} #finished time
g = {"A":["B"],  "B":["C","D","E"], "C":["E"], "D":["A","E"],"E":[]} # graph represent and I modified by adding "E:[]" in the graph

'''Initialize all vertices to white and set time to 0'''
def initialize():
    for v in g:
        if v not in c:
            c[v] = "white"
            a[v] = None

'''Traverse vertices'''
def dfs():
    for v in sorted(c.keys()):
        if c[v] == "white":
            dfs_visit(v)

'''Traverse Adj vertices and Identify Tree, Cross, And Forward Edges'''            
def dfs_visit(v,tab = 0):
    global time
    c[v] = "gray"
    d[v] = time
    time += 1
    for el in g[v]:
        if c[v] == "gray" and c[el] == "white":
            a[el] = v
            print '\t'*tab,v,"->",el
            dfs_visit(el,tab+1)
        elif c[v] == "gray" and c[el] == "gray":
            print '\t'*tab,"*",v,"->",el,"(back)"
        elif c[v] == "gray" and c[el] == "black" and d[v] > d[el]:
            print '\t'*tab,"*",v,"->",el,"(cross)"
        else:
            print '\t'*tab,"*",v,"->",el,"(forward)"
    c[v] = "black"
    f[v] = time
    time +=1
            
initialize()
dfs()
