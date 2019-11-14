#Compute the parity of a large 64-bit words
def brute_force(x):
	num = 0
	while x:
		num += x & 1
		x >>= 1
	
	return num % 2

def parity(x):
	result = 0
	while x:
		result ^= x & 1
		x >>= 1

	return result


def parity_v2(x):
	"""
	use the lowest set bit erased technique
	"""
	result = 0
	while x:
		result ^= 1
		x &= (x - 1) #drop the lowest set bit
	
	return result


def parity_v3(x):
	PRECOMPUTED_PARITY = [0, 1, 1, 0]
	MASK_SIZE = 16
	BIT_MASK = 0xFFFF



def parity_v4(x):
	print(bin(x))
	x ^= x >> 32 
	x ^= x >> 16 
	x ^= x >> 8 
	x ^= x >> 4 
	x ^= x >> 2 
	x ^= x >> 1 


	return x & 0x1




print(bin(1031))
print(brute_force(1031))
print(parity(1031))
print(parity_v2(1031))
print(parity_v4(217))
