# Iterative Python program to search an element



class Node:

	
	def __init__(self, data):
		self.data = data
		self.next = None 




class LinkedList:
	def __init__(self):
		self.head = None 
	
	def push(self, new_data):

		
		new_node = Node(new_data)

		
		new_node.next = self.head

		
		self.head = new_node

	
	def search(self, x):

		
		current = self.head

		
		while current != None:
			if current.data == x:
				return True

			current = current.next

		return False



if __name__ == '__main__':

	
	llist = LinkedList()

	''' Use push() to construct below list
		14->21->11->30->10 '''
	llist.push(10)
	llist.push(30)
	llist.push(11)
	llist.push(21)
	llist.push(14)


	if llist.search(99):
		print("Yes")
	else:
		print("No")


