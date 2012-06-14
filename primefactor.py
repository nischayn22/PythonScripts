def factor(a):
	if(a==1):
		return 1
	for i in reversed(range(1,int(math.sqrt(int(a))))):
		if (a%i==0 and factor(i)==1 ):
			return i

		
print factor(600851475143)