#!usr/bin/env python
color = {"CS10" : 0, "CS11": 0, "CS20" :0, "CS21" : 0, "CS12" : 0, "CS30":0}
time = {"CS10" : 0, "CS11": 0, "CS20" :0, "CS21" : 0, "CS12" : 0, "CS30":0}
graph = {"CS10" : ["CS11", "CS20"], "CS11" : ["CS21"], "CS20": ["CS30"], "CS21": ["CS12", "CS20"], "CS12":["CS30"],"CS30":[]}
in_degree ={"CS10" : 0, "CS11": 0, "CS20" :0, "CS21" :0, "CS12" : 0, "CS30":0}
timer = 0
path = "CS10"
def dfs(head, level):
	color[head] = 1
	global timer
	time[head] = timer;
	timer+=1
	if head not in graph:
		color[head] = 2
		return 
	for x in graph[head]:
		in_degree[x]-=1
		if color[x] == 0 and in_degree[x]==0:  
			global path
			path = path + "->" + x
			dfs(x, level+1)
		elif color[x] == 1 and in_degree[x]==0:
			path = path + "->" + x
		elif time[x] < time[head] and in_degree[x]==0: 
			path = path + "->" + x
	
	color[head] = 2
	return
for x in graph:
	for y in graph[x]:
		in_degree[y]+=1 
dfs("CS10", 0)
print path