import string

f = open('input.in', 'r')
f1 = open('output.out', 'r+')
N = f.readline()
N = int(N)
case = 0
while case<N:
	case = case + 1
	number = str(case)
	f1.write('Case #')
	f1.write(number)
	f1.write(': ')
	length = int(f.readline())
	str1 = f.readline()
	str2 = f.readline()
	str1 = str1.split()
	str2 = str2.split()
	str1.sort()
	str2.sort()
	position = 0
	sum = 0
	long(sum)
	option1 = 0
	long(option1)
	while position<length:
		position += 1
		min1 = str1[0]
		max2 = str2[-1]
		option1 = int(min1)*int(max2)
		sum += option1
		str1.pop(0)
		str2.pop(-1)
	f1.write(str(sum) +'\n')