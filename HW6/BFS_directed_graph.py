import Queue #FIFO (First In First Out) Queue

p = {} #ancestor
c = {} #color
d = {} #Level/Distance order
g = {"A":["B"],  "B":["C","D","E"], "C":["E"], "D":["A","E"],"E":[]} # graph represent and I modified by adding "E:[]" in the graph
back = []

'''Initialize all vertices to white and set time to 0'''
def foo(root):
    for u in g:
        c[u] = "white"
        d[u] = 0
        p[u] = None
    for v in sorted(g.keys()):
        foo2(v)

def foo2(v):
    c[v] = "gray"
    p[v] = None
    q = Queue.Queue()
    q.put(v)
    while not q.empty():
        u = q.get()
        q.put(u)
        for v in g[u]:
            if d[u] >= d[v]:
                back.append(u)
            print "color u ",u,c[u]
            print "color v ",v,c[v]
            if c[v] == "white":
                c[v] = "gray"
                d[v] = d[u]+1
                p[v] = u
                q.put(v)
        u = q.get()
        c[u] = "black"
        print "turn to black color u",u,c[u]
        
a = foo("A")
print c
print d
print p
print "back: ",back
            

# def initialize():
#     for v in g:
#         if v not in c:
#             c[v] = "white"
#             p[v] = None
#             d[v] = 10000 # Consider it as INFINITY
# 
# def bfs(g):
#     for v in sorted(c.keys()):
#         print "v: ",v
#         print "c: ",c
#         print "d: ",d
#         bfs_traverse(v)
# 
# '''Traverse vertices'''
# lev = 0
# def bfs_traverse(v):
#     global lev
# #     print d
# #     print c
#     c[v] = "gray"
#     d[v] = lev
#     p[v] = None
#     q = Queue.Queue()
#     q.put(v)
#     while not q.empty():
#         u = q.get()
# #         if u not in cache:
# #             cache.append(u)
# #         print "level u:" ,d[u]
# #         print "u",u
#         for v2 in g[u]:
# #             print "level v:" ,d[v2]
# #             print "v",v2
#             if c[v2] == "white":
#                 c[v2] = "gray"
#                 d[v2] = d[u]+1
#                 p[v2] = u
#                 q.put(v2)
#                 c[u] = "black"
#         q.get()
#    
# initialize()
# bfs(g)

