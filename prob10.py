import math
import time
s=time.time()
num = 1
def isPrime(number):
	for a in prime:
		if(a > (int(math.sqrt(number))+1)):
			return True
		if (number%a == 0):
			return False
	return True
prime = [2]
while(num<2000000-2):
	num = num+2
	if (isPrime(num)):
		prime.append(num)
sum =0
for sumer in prime:
	sum +=sumer
print sum
print time.time()-s