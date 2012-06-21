import math
import time
s=time.time()
num = 2
def isPrime(number):
	for a in prime:
		if(a > (int(math.sqrt(number))+1)):
			return True
		if (number%a == 0):
			return False
	return True

t=1
prime = [2]
while(t!=10001):
	num = num+1
	if (isPrime(num)):
		t = t+1
		prime.append(num)
print prime.pop()
print time.time()-s