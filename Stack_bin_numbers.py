#Converts decimal numbers to binary using the Python Stack
import stack as s
import pdb

def convert(decimal, base=2):
	stack = s.Stack()

	while decimal > 0:
		remainder = decimal%base
		stack.push(remainder)
		decimal = int((decimal/base))
	print(len(stack.items))
	return stack

def output_binary(binary_stack):
	
	final_string = [binary_stack.pop() for x in range(binary_stack.size())]
	
	return "".join(map(str, final_string))

if __name__ == '__main__':
	new_stack = convert(23,2)
	#pdb.set_trace()
	print(output_binary(new_stack))