n=200
vertex = range(1,n+1)
edge = {}
for i in vertex:
	edge[i] = raw_input().split()
	edge[i].pop(0)
dist = [1000000]*n
for i in edge[1]:
	a,b = map(int,i.split(','))
	dist[a-1] = b
while(len(vertex)!=0):
	x = min(vertex,key=lambda a: dist[a-1])
	vertex.remove(x)
	for i in edge[x]:
		a,b = map(int,i.split(','))
		# print dist
		# print dist[a-1]
		old = dist[a-1]
		new = dist[x-1]+b
		if(old > new):
			dist[a-1] = new
def anon(a):
	global dist
	print dist[a-1]
map(anon,[7,37,59,82,99,115,133,165,188,197])		