#https://www.spoj.com/problems/AKBAR/

def bfs(list_city, guard_per_city):
	visited = [False for _ in range(n)]
	




if __name__ == '__main__':
	testcase = int(input())
	for case in range(testcase):
		n, r, m = map(int, input().split())
		graph = [[] for i in range(n)]	
		visited = [False for _ in range(n)]
		guard_per_city = [0 for _ in range(n)]
		list_city = []
		for i in range(r):
			u, v = map(int, input().split())	
			graph[u-1].append(v-1)
			graph[v-1].append(u-1)
		for j in range(m):
			city, strength = map(int, input().split())
			list_city.append((city-1, strength))

		print(graph)
		print(city_guard)
		for i in range(m):
			flag = bfs(list_city[i], guard_per_city)
			if flag:
				break
		

		if flag:
			print('No')
		else:
			print('Yes')
		
			
			

