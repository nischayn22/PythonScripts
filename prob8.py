count = 0
numbers = []
f = open('input.txt','r')
while(count < 994):
	f.seek(count)
	a = f.read(1)
	count +=1
	if(a=='9'):
		# print "hsld"
		a = int(a)
		for i in range(1,5):
			a = 10 * a + int(f.read(1))
			#print i
		numbers.append(a)
print numbers
a=max(numbers)
numbers.remove(a)
b=max(numbers)
print a
print b
a=max(numbers)
numbers.remove(a)
b=max(numbers)
print a
print b
print 9*9*9*8*7