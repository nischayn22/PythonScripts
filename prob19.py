year = 1901
i = 1
count = 0
while(year<=2000):
	if(i==0):
		count +=1
	i=(i+31)%7
	if(i==0):
		count +=1
	if(year%4==0):
		i=(i+29)%7
		if(i==0):
			count +=1
	else:
		i=(i+28)%7
		if(i==0):
			count +=1
	i=(i+31)%7
	if(i==0):
		count +=1
	i=(i+30)%7
	if(i==0):
		count +=1
	i=(i+31)%7
	if(i==0):
		count +=1
	i=(i+30)%7
	if(i==0):
		count +=1
	i=(i+31)%7
	if(i==0):
		count +=1
	i=(i+31)%7
	if(i==0):
		count +=1
	i=(i+30)%7
	if(i==0):
		count +=1
	i=(i+31)%7
	if(i==0):
		count +=1
	i=(i+30)%7
	if(i==0):
		count +=1
	i=(i+31)%7
	year+=1
print count	