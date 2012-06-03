num = int(raw_input())
xcoord = []
ycoord = []
for x in range(num):
	a,b = map(int, raw_input().split())
	xcoord.append(a)
	ycoord.append(b)
times = int(raw_input())
for x in range(times):
	ch,m,n = raw_input().split()
	m = int(m)
	n = int(n)
	if(ch == 'Y'):
		for i in xrange(m-1,n):
			xcoord[i] = xcoord[i]*(-1)
		continue
	if(ch == 'X'):
		for i in xrange(m-1,n):
			ycoord[i] = ycoord[i]*(-1)
		continue
	if(ch == 'C'):
		a=b=c=d=0
		for i in xrange(m-1,n):
			if(xcoord[i]>0):
				if(ycoord[i]>0):
					a=a+1
				else:
					d=d+1
			elif(ycoord[i]>0):
				b=b+1
			else:
				c=c+1
		print a,b,c,d		
	