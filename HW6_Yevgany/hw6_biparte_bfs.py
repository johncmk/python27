#!usr/bin/env python
graph1 = {"A": ["D", "E"], "B": ["D"], "C": ["E"] ,"D":[], "E":[]}
graph = {"A": ["D", "E"], "B": ["D"], "C": ["A", "E"], "D":[], "E":[]}
level = {"A" : -1,"B" : -1, "C": -1, "D":-1, "E" : -1, "F" : -1}
color = {"A" : -1,"B" : -1, "C": -1, "D":-1, "E" : -1, "F" : -1}
biparte = False
q =[]
def bfs():
	 while q != []:
	 	node = q.pop(0)
	 	for  x in graph[node]:
	 		if level[x] == -1:
	 			q.append(x)
	 			level[x] = level[node]+1
	 		if color[x] == -1:
	 			color[x] = 1 - color[node]
	 		elif color[x] == color[node]:
	 			global biparte 
	 			biparte = True
	

bfs()
for x in graph:
	if level[x] == -1:
		q.append(x)
		color[x] =1
		bfs()
if biparte == True :
	print "Graph is not biparte"
else:
	for x in graph:
		left = []
	right = []
	for x in graph:
		if color[x] == 1:
			left.append(x)
		elif color[x] == 0:
			right.append(x)
	print "Left: " + str(left) + " " + "Right: " + str(right)
