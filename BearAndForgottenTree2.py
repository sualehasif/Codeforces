
import queue
adj = {}
x = input()
n, m, k = map(int, x.split(" "))

for i in range(n):
	adj[i] = []

for i in range(m):
	x = input()
	a, b = map(int, x.split())
	adj[a-1].append(b-1)
	adj[b-1].append(a-1)


visited = {}
q = queue.Queue(maxsize= 300000)

for i in range(n):
	visited[i] = False

q.put(0)

while not q.empty():
	s = q.get()
	for i in range(n):
		if visited[i] == False:
			if i not in adj[s]:
				visited[i] = True
				q.put(i)




connnected = True

for i in range(n):
	if visited[i] == False:
		connnected = False


if connnected:
	print("possible")
else:
	print("impossible")