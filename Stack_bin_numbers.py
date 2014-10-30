#Converts decimal numbers to binary using the Python Stack
import stack as s
import pdb
import random

def convert(decimal, base=2):
	stack = s.Stack()

	while decimal > 0:
		remainder = decimal%base
		stack.push(remainder)
		decimal = int((decimal/base))

	return stack

def output_binary(binary_stack):
	
	final_string = [binary_stack.pop() for x in range(binary_stack.size())]
	
	return "".join(map(str, final_string))

if __name__ == '__main__':
	#Tests Convert binary function on 100 random
	i=0
	while i < 100:
		test = random.randint(0,1000000)
		assert bin(test)[2:] == output_binary(convert(test)), "Test Failed"
		print("Binary = %s" %bin(test)[2:] )
		print("My Binary = %s" % output_binary(convert(test)))
		i += 1
	