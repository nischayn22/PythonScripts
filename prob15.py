cache = []
for i in range(20):
	cache.append([])
	for j in range(20):
		cache[i].append(0)

def step(i,j):
	if(i==20 or j==20):
		return 1
	if(cache[i][j]>0):
		return cache[i][j]
	cache[i][j] = step(i+1,j)+step(i,j+1)
	cache[j][i] = cache[i][j]
	return cache[i][j]
print step(0,0)