#!usr/bin/env python
graph = {"A" : ["B"], "B" : ["C", "D", "E"], "C": ["E"], "D": ["A", "E"], "E":[]}
level = {"A" : 0,"B" : -1, "C": -1, "D":-1, "E" : -1, "F" : -1}
back = []
cross = []
q = ["A"]
path = ""

def bfs():
	while q != []:
		node = q.pop(0)
		global path 
		path = path + node + " "
		for  x in graph[node]:
			if level[x] == -1:
				q.append(x)
				#print q
				level[x] = level[node]+1
			elif level[node] <= level[x]+1:
				cross.append(node + "->" + x)
			else:
				back.append(node + "->" + x)

bfs()
print "Path: ", path
print "Back: ", back
print "Cross: ", cross	