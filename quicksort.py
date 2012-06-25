array = {}
x=0
def lquick(array, m, n):
	global x
	pivot = m
	i = m+1
	if(n<=m):
		return
	x = x+(n-m)
	# print x
	mid = m+(n-m)/2
	#stupidest code I am ever writing zzz...
	if(array[mid]>array[n] and array[mid]<array[m]):
		temp = array[mid]
		array[mid] = array[m]
		array[m] = temp
	if(array[mid]>array[m] and array[mid]<array[n]):
		temp = array[mid]
		array[mid] = array[m]
		array[m] = temp
	if(array[n]>array[mid] and array[n]<array[m]):
		temp = array[n]
		array[n] = array[m]
		array[m] = temp
	if(array[n]>array[m] and array[n]<array[mid]):			
		temp = array[n]
		array[n] = array[m]
		array[m] = temp
	for j in range(m+1,n+1):
		if(array[j]<array[pivot]):
			if(i!=j):
				temp = array[i]
				array[i] = array[j]
				array[j] = temp
			i+=1
	temp = array[pivot]
	array[pivot] = array[i-1]
	array[i-1] = temp
	lquick(array,m,i-2)
	lquick(array,i,n)
for i in range(10000):
	array[i] = int(raw_input())
lquick(array,0,len(array)-1)
print x
