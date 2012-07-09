import time
now = time.time()
n = []
for i in range(100):
	n.append(map(int,raw_input().split()))
newresult = [int(59)]
n.pop(0)
for i in range(99):
	x = n.pop(0)
	result = list(newresult)
	newresult =[]
	t = len(x)
	for j in range(t):
		if(j==0):
			newresult.append(result[0]+x.pop(0))
		elif(j==t-1):
			newresult.append(result[0]+x.pop(0))
		else:
			newresult.append(max((result.pop(0)+x[0]),result[0]+x.pop(0)))
print max(newresult)
print time.time()-now