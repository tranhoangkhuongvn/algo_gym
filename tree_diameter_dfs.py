#https://leetcode.com/contest/biweekly-contest-12/problems/tree-diameter/


def dfs(node, prev, length):
	if len(graph[node])	== 1 and graph[node][0] == prev and length > res[0]: #leaf node
		res[0] = length
		res[1] = node
		print('res: ', res)	


	for v in graph[node]:
		if v != prev:
			print('DFS at v: ', v, length+1)
			dfs(v, node, length+1)

	
	
if __name__ == '__main__':
	edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
	res = [0, None]
	
	graph = [[] for _ in range(len(edges)+1)] 
	for u, v in edges:
		graph[u].append(v)
		graph[v].append(u)
	
	print('Pick {} as the starting point'.format(edges[0][0]))
	dfs(edges[0][0], None, 0)
	
	print('Pick {} as the next point'.format(res[1]))
	dfs(res[1], None, 0)
	
	print(res[0])
