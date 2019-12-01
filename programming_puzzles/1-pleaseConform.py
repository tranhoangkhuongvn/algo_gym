
def pleaseConform(cap_list):
	"""
	This function prints out the commands to tell people at 
	position i to flip their caps (either F or B)
	Goal is to print in least number of commands so all people 
	in line have same cap orientation
	"""
	if len(cap_list) == 0:
		print('Empty line')
		return

	cap_intervals = [] #each item in the list (start, end, cap_type)
	start = 0
	end = 0
	F_count = 0
	B_count = 0
	prev_cap_type = cap_list[0] 
	#cap_list = cap_list + ['END']
	if cap_list[0] == 'F':
		F_count = 1
		B_count = 0
	else:
		B_count = 1
		F_count = 0
	for i in range(1, len(cap_list)):
		if cap_list[i] != prev_cap_type:
			if cap_list[i] == 'F':
				F_count += 1
			else:
				B_count += 1
			end = i - 1
			cap_intervals.append((start, end, prev_cap_type))
			start = i
			prev_cap_type = cap_list[i]
		
		if i == len(cap_list) - 1:
			end = i
			prev_cap_type = cap_list[i]
			cap_intervals.append((start, end, prev_cap_type))

	print(cap_intervals)
	print(F_count, B_count)
	if F_count <= B_count:
		#switch everyone from F to B
		printCommands('F', cap_intervals)	
	else:
		printCommands('B', cap_intervals)

def printCommands(cap_type, cap_intervals):
	for start, end, cap in cap_intervals:
		if cap == cap_type:
			if start == end:
				print('People in position {}, please flip your cap'.format(start))
			else:
				print('People in position {} to {}, please flip your cap'.format(start, end))


if __name__ == '__main__':
	cap1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 
			'B', 'B', 'F', 'F', 'B', 'F']

	cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 
			'B', 'B', 'F', 'F', 'F', 'F']
	pleaseConform(cap2)
