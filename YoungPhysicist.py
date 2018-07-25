n = int(input())
x = []

for i in range(n):
	a = str(input())
	b = [int(i) for i in a.split()]
	
	x.append(b)

check = True

for i in range(2):
	s = 0
	for j in range(n):
		s += x[j][i]
	if s!= 0:
		check = False

if check:
	print("YES")
else:
	print("NO")
