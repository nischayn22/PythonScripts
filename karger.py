import random
n=200
set = range(1,n+1)
points = {}
for i in range(0,n):
	points[i] = map(int,raw_input().split())
	points[i].pop(0)
# print set
for i in range(0,n-2):
	x = random.randint(0,len(set)-1)
	# print x
	x = set[x]
	y = random.randint(0,len(points[x-1])-1)
	# print x,y
	y = points[x-1][y]
	# print x,y
	set.remove(y)
	for j in points[y-1]:
		points[j-1]=map(lambda a: x if a==y else a,points[j-1])
		# print points
#		points[j-1].remove(y)
	points[x-1] = points[x-1]+points[y-1]
	points[x-1]=filter(lambda a: a!=x,points[x-1])
	del points[y-1]
	# print points
# print set
# print points
print len(points[set[0]-1])