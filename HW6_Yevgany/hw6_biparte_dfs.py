#!usr/bin/env python
color = {"A":0,"B":0,"C":0,"D":0,"E":0}
color1 = {"A":-1,"B":-1,"C":-1,"D":-1,"E":-1}
graph1 = {"A": ["D", "E"], "B": ["D"], "C": ["A", "E"]}
graph = {"A": ["D", "E"], "B": ["D"], "C": ["E"] ,"D":[], "E":[]}
biparte = False
def dfs(head, level):
	color[head] = 1
	if head not in graph:
		color[head] = 2
		return 
	for x in graph[head]:
			dfs(x, level+1)
			if color1[x] == -1:
				color1[x] = 1 - color1[head]
			elif  color1[x] == color1[head]:
				global biparte
				biparte = True
				return 
	color[head] = 2
	return


for x in graph:
	if (color[x] == 0):
		color1[x] = 1
		dfs(x, 0)
if biparte == True :
	print "Not biparte"
else:
	left = []
	right = []
	for x in graph:
		if color1[x] == 1:
			left.append(x)
		elif color1[x] == 0:
			right.append(x)
	print "Left: " + str(left) + " " + "Right: " + str(right)  
#print color
#print color1