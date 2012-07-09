a = raw_input()
a = a.split(',')
a.sort()
sum = int(0)
pos = int(0)
for i in a:
	pos+=1
	score = int(0)
	for j in i:
		score+=(ord(j)-ord('A')+1)
	sum+=(pos*score)
print sum
	