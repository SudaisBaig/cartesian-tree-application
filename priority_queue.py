
# This file contains just a class of Priority Queue
# This is general Priority Queue and is accessed by method of priority queue which is defined inside cartesian tree class

class PriorityQueue(object):
	def __init__(self):
		self.queue = []

	def __str__(self):
		return ' '.join([str(i) for i in self.queue])

	def isEmpty(self):
		return len(self.queue) == 0


	def insert(self, data):
		self.queue.append(data)

	def get(self):
		return self.queue.pop()
    

	def delete(self):
		try:
			max = 0
			for i in range(len(self.queue)):
				if float(self.queue[i].value) > float(self.queue[max].value):
					max = i
			item = self.queue[max]
			del self.queue[max]
			return item
		except IndexError:
			print()
			exit()

if __name__ == '__main__':
	myQueue = PriorityQueue()
	myQueue.insert(12)
	myQueue.insert(1)
	myQueue.insert(14)
	myQueue.insert(7)
	print(myQueue)			
	while not myQueue.isEmpty():
		print(myQueue.delete())
