#http://acm.timus.ru/problem.aspx?space=1&num=1104

digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
if __name__ == '__main__':
	text = list(input())
	n = len(text)
	for k in range(3, 37):
		sum_val = 0
		base = n - 1
		for i in text:
			sum_val += (digits.index(i) % k)*(k)**(base)
			print(i, k, base, sum_val)
			base -= 1
		
		if sum_val % (k-1) == 0:
			print(k)
			exit(0)
			
	print('No solution')
			
		


