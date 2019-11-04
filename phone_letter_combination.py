
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
	result = []
	current_index = 0
	def conversion(ins, ans, current_index, result):
		n = len(ins)
		if len(ans) == n:
			result.append(ans)	
			print(ans)
			print(result)
			return result 

		
		num = ins[current_index]
		possible_char = list(number_letter_map[num])
		
		for j in range(len(possible_char)):
			ans.append(possible_char[j])
			temp = conversion(ins, ans, current_index+1, result)
			if temp and len(temp) == 2:
				result.append(temp)
			ans.pop()

		return None 


	result = conversion(ins, ans, current_index, result)
	
	for res in result:
		print(res)

	return result


print(solution())
