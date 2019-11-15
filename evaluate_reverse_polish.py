def evalRPN(tokens):
	"""
	:type tokens: List[str]
	:rtype: int
	"""
	operators = ['+', '-', '/', '*']
	num_list = []
	n = len(tokens)
	i = 0
	for i in range(len(tokens)):
		if tokens[i] not in operators:
			num_list.append(tokens[i])
			
		else:
			try:
				second = int(num_list.pop())
				first = int(num_list.pop())
				
			except:
				print('not enough element')
				break
			
			temp = 0
			if tokens[i] == '+':
				temp = first + second
			elif tokens[i] == '-':
				temp = first - second
			elif tokens[i] == '*':
				temp = first * second
			elif tokens[i] == '/':
				temp = int(first / second)
				print(int(first/second))
			num_list.append(temp)
		print(num_list)
	
	return num_list[0]

ins = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(evalRPN(ins))
