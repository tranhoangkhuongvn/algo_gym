#https://leetcode.com/problems/reverse-bits/


def reverse_bit(n):
	output = 0

	for i in range(32):
		output = output | (n & 1)
		n >>= 1
		output <<= 1

	print(bin(output >> 1))
	return output >> 1


n = 4294967293
print('original: ', bin(n))
print(reverse_bit(n))
