#!/usr/bin/env python

__author__ = "CS381 John Advanced Programming"

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
            detect_cycle(v)

'''Traverse Adj vertices and Identify Tree, Cross, And Forward Edges'''            
def detect_cycle(v,tab = 0):
    c[v] = "gray"
    for el in g[v]:
        if c[v] == "gray" and c[el] == "white":
            a[el] = v
            print v,"->",
            detect_cycle(el,tab+1)
        elif c[v] == "gray" and c[el] == "gray":
            print el
        return
            
initialize()
dfs()
