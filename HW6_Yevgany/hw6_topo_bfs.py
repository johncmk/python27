#!usr/bin/env python
graph = {"CS10" : ["CS11", "CS20"], "CS11" : ["CS21"], "CS20": ["CS30"], "CS21": ["CS12", "CS20"], "CS12":["CS30"],"CS30":[]}
level = {"CS10" : 0, "CS11": -1, "CS20" :-1, "CS21" : -1, "CS12" : -1, "CS30":-1}
in_degree ={"CS10" : 0, "CS11": 0, "CS20" :0, "CS21" :0, "CS12" : 0, "CS30":0}
back = []
cross = []
q = ["CS10"]
path = ""

def bfs():
	 while q != []:
	 	node = q.pop(0)
	 	global path 
	 	if path is "":
	 		path = path + node
	 	else:
			path = path + " -> " + node
	 	for  x in graph[node]:
	 		in_degree[x] -= 1
	 		if level[x] == -1 and in_degree[x] == 0:
	 			q.append(x)
	 			#print q
	 			level[x] = level[node]+1

for x in graph:
	for y in graph[x]:
		in_degree[y]+=1

bfs()
print path
