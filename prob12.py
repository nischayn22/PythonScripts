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
prime =[list all primes here]
n=9909900
expcount  = 1
for primenum in prime:
	count = 1
	if primenum>n+1:
		break
	if(primenum ==2):
		count =0
	# print primenum
	n1 = n
	n2 = n+1
	while(n1%primenum==0):
		count+=1
		n1/=primenum
	while(n2%primenum==0):
		count+=1
		n2/=primenum
	# print count,primenum
	expcount*=count
# print prime
print expcount
print time.time()-s