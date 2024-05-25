class BinaryTree:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		
	def put(self, key, value):
		if self.key == key:
			self.value = value
		if self.key > key:
			if self.left == None:
				self.left = BinaryTree(key, value)
			else:
				self.left.put(key, value)
		if self.key < key:
			if self.right == None:
				self.right = BinaryTree(key, value)
			else:
				self.right.put(key, value)
		return
		
	# percorrer a arvore
	def get_bt(self, key):
		if self.key == key:
			return self.value
		elif self.key > key and self.left is not None:
			return self.left.get_bt(key)
		elif self.key < key and self.right is not None:
			return self.right.get_bt(key)
		else:
			return None
		
	def print(self):
		print("(", end='')
		if self.left != None:
			self.left.print()
		print(str(self.key) + " " + str(self.value), end = '')
		if self.right != None:
			self.right.print()
		print(")", end='')
		
	"""
BT = BinaryTree("Joao", 3)
BT.put("ad", 4)
BT.put("ga", 2)
BT.put("Joaa", 4)

BT.print()
print()
"""
		
		
		
		
		
		
		
		
		
		
		
		
		
