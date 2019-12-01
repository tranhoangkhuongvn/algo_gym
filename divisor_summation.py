import math



if __name__ == '__main__':
	testcase = int(input())
	for case in range(testcase):
		n = int(input())
		sum_val = 0
		for i in range(1, n//2 + 1):
			if n % i == 0:
				sum_val += i

		print(sum_val)
