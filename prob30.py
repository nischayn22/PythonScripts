#logic from blogs
from math import pow
powers = {}
count = 0
for i in range(0,10):
	powers[str(i)] = pow(i,5)
print powers
for i in xrange(2,354294):
	total = 0
	for j in str(i):
		total+=powers[j]
	if total==i :
		count+=i
#		print i
print count