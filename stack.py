#implementa stack data structure in python

class Stack():
	def __init__(self):
		self.items = []

	def push(self, item):
		return self.items.append(item)

	def pop(self):
		return self.items[-1]

	def peek(self):
		new = self.items[-1]
		return new

	def isEmpty(self):
		return len(self.items) == 0

	def size(self):
		return len(self.items)


if __name__ == '__main__':

	test_list = [x for x in range(10) if x%2==0]

	test_stack = Stack()

	print(test_stack.isEmpty())

	[test_stack.push(x) for x in test_list]

	print(test_stack.peek())
	print(test_stack.size())
	print(test_stack.isEmpty())
