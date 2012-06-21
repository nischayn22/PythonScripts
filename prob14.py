def collatz(i):
	global cache
	if(str(i) in cache):
		return cache[str(i)]
	if(i%2==0):
		cache[str(i)] = 1+collatz(i/2)
		return cache[str(i)]
	cache[str(i)] = 1+collatz(i*3+1)
	return cache[str(i)]
cache = {'1': 1}
maximum = 0
for i in range(1,1000000):
	maximum = max(maximum,collatz(i))
# print cache
for k,v in cache.iteritems():
	if(v==maximum):
		print k
		exit()
