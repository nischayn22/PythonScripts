sum = int(1)
add = int(2)
pos = int(1)
n = int(raw_input())
while(add<=n):
	for i in xrange(4):
		pos+=add
		sum+=pos
	add+=2
print sum