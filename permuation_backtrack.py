def A_n_k(a, n, k, depth, used, curr, ans):
	if depth == k:
		ans.append(curr)
		print('At depth {}: {}'.format(depth,ans))
		return 

	for i in range(n):
		if not used[i]:
			curr.append(a[i])
			used[i] = True 
			print(curr)
			A_n_k(a, n, k, depth+1, used, curr, ans)

			curr.pop()
			print('backtrack: ', curr)
			used[i] = False 
			print('used: ', used)	
	return 


a = [1,2,3]
n = len(a)

used = [False] * len(a)
ans = []
A_n_k(a, n, n, 0, used, [], ans)
for an in ans:
	print(an)
