#Linked List in Python
#Implemented as a class with next and previous data attributes and several methods
import pdb

class Node(object):
	def __init__(self, node_data):
		self.data = node_data
		self.next = None
		self.previous = None

	def getData(self):
		print(self.data)
		return self.data

	def getNext(self):
		return self.next

	def setData(self, newData):
		self.data = newData

	def setNext(self, next):
		self.next = next

	def getPrev(self):
		return self.previous

	def setData(self, newData):
		self.previous = newData

class Linked_List(object):
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self, new_node):
		''' adds a new node to the beginning of the list''' 
		new_node.setNext(self.head)
		self.head = new_node
		if self.head != None:
			self.head.previous = new_node
			


	def size(self):
		'''counts number of nodes in the list '''
		next = self.head
		size = 0
		while next != None:
			size += 1
			next = next.getNext()
		return size

	def search(self, search_value):
		'''finds a specific value in the list '''
		found = False
		next = self.head
		count = 0
		while next.next != None and next.data != search_value:
			count += 1
			next = next.getNext()
		return next, count

	def remove(self, remove_value):
		'''removes specified value from the linked list '''
		current = self.head
		remove = False

		future = current.getNext()

		while not remove:
			if current.data == remove_value:
				remove = True
				if current.previous == None:
					self.head = current.getNext()
				else:
					current.previous.setNext(current.getNext())
					current.getNext().previous = current.previous
			else:
				current = current.getNext()

	def insert(self, new_item, position):
		'''adds a new item into a specific position'''
		temp = self.index(position)
		print(temp.data)
		if temp.previous != None:

			new_item.previous = temp.previous

		new_item.next = temp.next
		temp.previous = new_item
		temp.previous.next = new_item



	def index(self, count):
		''' returns node of an index in linked list with 0 being the head '''
		start = self.head
		while count > 0:
			start = start.getNext()
			count -= 1
		print(type(start))
		return start





if __name__ == '__main__':
	llist = Linked_List()
	test = Node(100)
	test2 = Node(200)
	print(test.data)
	llist.add(test)
	#pdb.set_trace()

	#assert llist.size() ==1, "Size of list Calculating Incorrectly"
	llist.add(test2)
	llist.head.getData()
	print(llist.index(0).data)
	llist.insert(Node(300),2)
	print(llist.head.data)




