time = 1
a = {} #ancestor
c = {} #color
d = {} #discovered time
f = {} #finished time
g = {"A":["B"],  "B":["C","D","E"], "C":["E"], "D":["A","E"],"E":[]} # graph represent

def traverse(g,s,e,path = []):
    path = path + [s]
    if s == e:
        return path
    if not g.has_key(s):
        return None
    for v in g[s]:
        if v not in path:
            newPath = traverse(g,v,e,path)
            if newPath:
                return newPath
    return None

'''Initialize all vertices to white and set time to 0'''
def initialize():
    for v in g:
        if v not in c:
            c[v] = "white"
            a[v] = None
        for el in g[v]:
            if el not in c:
                c[el] = "white"
                a[el] = None

def dfs():
    for v in sorted(c.keys()):
        if c[v] == "white":
            dfs_visit(v)
            
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
            
# initialize()
# dfs()
print traverse(g,"A","D")
