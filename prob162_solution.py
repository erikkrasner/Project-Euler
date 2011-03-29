#!/usr/bin/env python
# 3D58725572C62302
# 0.056s

def num_hex_numbers_with_01a(num_digits):
	total = 0
	none,z,one,a,z1,za,a1,za1=13,0,1,1,0,0,0,0
	for extra_digit in range(1,num_digits):
		old_none,old_z,old_one,old_a,old_z1,old_za,old_a1,old_za1 =\
			none,z,one,a,z1,za,a1,za1
		none = 13 * old_none
		z = 14 * old_z + old_none
		one = 14 * old_one + old_none
		a = 14 * old_a + old_none
		z1 = 15 * old_z1 + old_z + old_one
		za = 15 * old_za + old_z + old_a
		a1 = 15 * old_a1 + old_a + old_one
		za1 = 16 * old_za1 + old_z1 + old_za + old_a1
		total += za1
	return total

def euler_format(solution):
    return `hex(solution)`[3:-2].upper()

if __name__ == '__main__':
    print euler_format(num_hex_numbers_with_01a(16))
