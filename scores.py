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
	words = words.split()
	
	googlers = int(words[0])
	
	suprises = int(words[1])
	p = int(words[2])
	
	count = 0
	points = int(0)
	#f1.write('hello')
	while googlers>0:
		
		googlers = googlers - 1
		points = int(words[3+googlers])
		if (points/3)>=p:
			count = count + 1
		#	f1.write(str(count))

			continue
		elif (3*p)-points<=2:
			count = count +1
			continue
		elif (((3*p)-points==3) or ((3*p)-points==4)) and p>1:
			if suprises>0 and suprises!=0:
				count = count +1
				suprises = suprises -1
		
		
	f1.write('Case #')
	f1.write(number)
	f1.write(': ')
	f1.write(str(count))
	if case!=N:	
		f1.write('\n')
