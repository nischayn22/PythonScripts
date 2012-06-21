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
while(num!=998):
	num = num+1
	if (isPrime(num)):
		t = t+1
		prime.append(num)
# print prime
x=y=z=9
number = 100001*x+10010*y+1100*z
for x in reversed(range(0,10)):
	for y in reversed(range(0,10)):
		for z in reversed(range(0,10)):
			number = 100001*x+10010*y+1100*z
			for b in reversed(range(100,999)):
				if(number%b==0 and number/b in range(100,999)):
					print number
					print "the divisor is %d and qu is %d " % (b,number/b)
					print time.time()-s
					exit()
