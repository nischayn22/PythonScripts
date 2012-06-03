import string

f = open('input.in', 'r')
f1 = open('output.out', 'r+')
N = f.readline()
N = int(N)
case = 0
while case<N:
	
	case = case + 1
	number = str(case)
	words = f.readline()
	transform = ['y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q']
	newwords = ''
	for c in words:
		key = ord(c)-97
		if key==(-65):
			print key	
			newwords = newwords + ' '
		elif key>=0:
			newwords = newwords + transform[key]
	f1.write('Case #')
	f1.write(number)
	f1.write(': ')
	f1.write(newwords)
	if case!=N:	
		f1.write('\n')
