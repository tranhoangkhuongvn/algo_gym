



if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		n, x = map(int, input().split())
		arr = list(map(int, input().split()))
		s = set()
		for e in arr:
			s.add(e)
		if len(s) == x:
			print('Good')
		elif len(s) > x:
			print('Average')
		else:
			print('Bad')
