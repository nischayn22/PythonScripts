import time,sys,threading
threading.stack_size(67108864)
sys.setrecursionlimit(2 ** 20)
# n = 9
# k = 11
n = 875714
k = 5105043
t=0
def revdfs(a):
	global t,revedges,visittime,visited
	if visited[a]==True:
		return
	visited[a] = True
	for i in revedges[a]:
		revdfs(i)
	t +=1
	visittime[a] = t
	return

def dfs(a):
	global edges,count,visited
	if visited[a]==False :
		return
	visited[a] = False
	for i in edges[a]:
		dfs(i)
	count +=1
	return
s=time.time()
vertex = range(1,n+1)
edges = {}
revedges = {}
visited = {}
visittime = {}
maxsccs = []
count = 0
def main():
	global vertex,edges,s,revedges,visited,visittime,maxsccs,count
	for i in vertex:
		edges[i] = []
		revedges[i] = []
		visited[i] = False
	for i in range(1,k+1):
		a,b = map(int,raw_input().split())
		edges[a].append(b)
		revedges[b].append(a)
	print time.time()-s
	for i in reversed(vertex):
		if visited[i] == False :
			revdfs(i)
	del revedges
	print time.time()-s
	vertex.sort(key=lambda z: visittime[z])
	for i in reversed(vertex):
		if visited[i] == True:
			count = 0
			dfs(i)
			maxsccs.append(count)
	maxsccs.sort()
	print maxsccs.pop()
	print maxsccs.pop()
	print maxsccs.pop()
	print maxsccs.pop()
	print maxsccs.pop()
	print maxsccs.pop()
	print time.time()-s
	return
thread = threading.Thread(target = main) # instantiate thread object
thread.start() # run program at target