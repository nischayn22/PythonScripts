from math import sqrt
a = int(10)
for i in range(999):
	a*=10
t = 1
while(t!=0):
	b=sqrt(5*a*a+4)
	c=b-int(8)
	if(b==int(b) or c==int(c)):
		t=0
	else:
		a+=1
print a