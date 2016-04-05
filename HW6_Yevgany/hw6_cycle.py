#!usr/bin/env python
color = {"A":0,"B":0,"C":0,"D":0,"E":0}
time = {"A":0,"B":0,"C":0,"D":0,"E":0}
graph = {"A": ["B"], "B": ["C", "D", "E"], "C": ["E"], "D": ["A", "E"]}
graph1 = {"A": ["B"], "B": ["C", "D", "E"], "C": ["E"], "D": ["E"]}
timer = 0
path = []
back = False
def dfs(head, level):
	color[head] = 1
	global timer
	time[head] = timer;
	timer+=1
	global path
	if head not in graph:
		color[head] = 2
		return  
	path.append(head)
	for x in graph[head]:
		if color[x] == 0:  #grey to white
			#print '     '*level, head,"->",x 
			dfs(x, level+1)
		elif color[x] == 1: #grey to grey
			global back
			back = True
			path.append(x)
			return 
	color[head] = 2
	return

dfs("A", 0)
copied_path = path[:]
if back is False:
	print "ACYCLIC"
else:
	cycle =""
	for i,x in enumerate(range(len(path)-1)):
		if path[x+1] not in graph[path[i]]:
			copied_path.remove(path[i])
	for x in range(len(path)-2):
		cycle =cycle + copied_path[x] + "->"
	print cycle + path[len(path)-1]