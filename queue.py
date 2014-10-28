#Implementation of a queue Abstract Data Type in Python
#Implementation uses a list structure 
#List constantly grows
#has a pointer to "Rear" and "First item"
# first item is the most recently added item in the list (the end)
#This allows us to implement enqueue (add stuff to the list) in O(1)
#Indexing is also O(1) so removing stuff from queue is also O(1)

class Queue(object):
	def __init__(self):
		self.items = list()
		self.head = 0
		self.tail = 0

	def isEmpty(self):
		return self.tail == self.head

	def enqueue(self, new_item):
		self.items.append(new_item)
		self.head+=1

	def dequeue(self):
		if self.tail >= self.head:
			raise ValueError
		else:
			self.tail += 1
			return self.items[self.tail-1]

	def size(self):
		return self.head - self.tail +1


if __name__ == '__main__':
	q = Queue()

	assert q.isEmpty()==True, 'Size is not working'
	q.enqueue("Cat")
	assert q.isEmpty()==False, 'Size is not working'
	q.dequeue()
	
	try:
		q.dequeue()
		print("Not working")
	except ValueError:
		print("Passed")


