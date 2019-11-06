#http://acm.timus.ru/problem.aspx?space=1&num=1086
import math


def is_prime(n):
	if n < 2:
		return False

	for i in range(1, int(math.sqrt(n))+1):
		if i != 1 and n % i == 0:
			return False 
	
	return True


if __name__ == '__main__':
	t = int(input())
	arr = []
	for _ in range(t):
		arr.append(int(input()))

	prime_arr = [0]
	for i in range(0, 164000):
		if is_prime(i):
			prime_arr.append(i)
	for e in arr:
		print(prime_arr[e])
	
