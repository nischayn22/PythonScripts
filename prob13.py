from math import pow
numbers = []
f = open("input.txt",'r')
for i in range(0,100):
	number = int(str(f.readline()[:50]))
	numbers.append(number)
print number
x=y=int(0)
for i in range(0,100):
	for num in numbers:
		x +=num
print x