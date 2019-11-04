
def solution():
	number_letter_map = {
		'2': 'abc',
		'3': 'def',
		'4': 'ghi',
		'5': 'jkl',
		'6': 'mno',
		'7': 'pqrs',
		'8': 'tuv',
		'9': 'wxyz'
	}

	ins = '23'
	ans = []
	current_index = 0
	def conversion(ins, ans, current_index):
		print(ans)
		n = len(ins)
		if len(ans) == n:
			result.append(ans)	
			print('Result:', result)	
		else:
		
			num = ins[current_index]
			possible_char = list(number_letter_map[num])
			print(num, possible_char)	
			for j in range(len(possible_char)):
				ans.append(possible_char[j])
				conversion(ins, ans, current_index+1)
				ans.pop()
			
		

	result = []
	conversion(ins, ans, current_index)
	

	return result


print(solution())
