import string

f = open('input.in', 'r')
f2 = open('output.out', 'w')
N = f.readline()
case = 0
while case<N:
	case = case + 1
	words = f.readline()
	words = words.split()
	f1.write('case#'.case.': ')
	for i in reversed(words):
		f1.write(i)
	f1.write('\n')
