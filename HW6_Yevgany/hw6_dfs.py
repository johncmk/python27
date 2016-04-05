color = {"A":0,"B":0,"C":0,"D":0,"E":0}
time = {"A":0,"B":0,"C":0,"D":0,"E":0}
graph = {"A": ["B"], "B": ["C", "D", "E"], "C": ["E"], "D": ["A", "E"]}
timer = 0

def dfs(node, level):
	color[node] = 1
	global timer
	time[node] = timer;
	timer+=1
	if node not in graph:
		color[node] = 2
		return 
	for x in graph[node]:
		if color[x] == 0:  
			print '     '*level, node,"->",x
			dfs(x, level+1)
		elif color[x] == 1: 
			print '     '*level, "*", node,"->",x,"(back)"
		elif time[x] < time[node]:
			print '     '*level, "*", node,"->",x,"(cross)"
		else:
			print '     '*level, "*", node,"->",x,"(forward)"
	color[node] = 2
	return

dfs("A", 0)