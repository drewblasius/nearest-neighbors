class Node(object):
	def __init__(self,axis=None,parent=None,data=None):	
		self.setAxis(axis)
		self.setData(data)
		self.setParent(parent)
		self.setLeft(None)
		self.setRight(None)

	def setLeft(self,left):
		self.__left = left

	def getLeft(self):
		return self.__left

	def setRight(self,right):
		self.__right = right

	def getRight(self):
		return self.__right
	
	def setParent(self,parent):
		self.__parent = parent
	
	def getParent(self):
		return self.__parent
	
	def setData(self,data):
		self.__data = data
	
	def getData(self):
		return self.__data

	def setAxis(self,axis):
		self.__axis = axis

	def getAxis(self):
		return self.__axis

	def setNext(self,nextNode):
		if self.getAxis() is None:
			raise ValueError("Axis needs to be set before use!")
		data = nextNode.getData()
		axis = self.getAxis()
		if self.getData()[axis] > data[axis]:
			self.setRight(nextNode)
		elif self.getData()[axis] < data[axis]:
			self.setLeft(nextNode)
		nextNode.setParent(self)

	def getNext(self,testNode):
		if self.getAxis() is None:
			raise ValueError("Axis needs to be set before use!")
		data = testNode.getData()
		axis = self.getAxis()
		if self.getData()[axis] > data[axis]:
			return self.getRight()
		elif self.getData()[axis] < data[axis]:
			return self.getLeft()
		else:
			return None

	def getOpposite(self,testNode):
		# given a test node, returns OPPOSITE of the next node
		if self.getAxis() is None:
			raise ValueError("Axis needs to be set before use!")
		data = testNode.getData()
		axis = self.getAxis()
		if self.getData()[axis] > data[axis]:
			return self.getLeft()
		elif self.getData()[axis] < data[axis]:
			return self.getRight()
		else:
			return None


class kdTree(object):
    def __init__(self):
    	pass

    def setRoot(self,root):
    	self.__root = root

    def getRoot(self):
    	return self.__root

    def setDim(self,dim):
    	self.__dim = dim

    def getDim(self):
    	return self.__dim

    def d(self,xNode,yNode):
    	pass

    def dAbs(self,searchNode,axisNode):
    	pass

    def insertNode(self,node):
    	if self.getRoot() is None:
    		self.setRoot(node)
    		self.getRoot().setAxis(0)
    	else:
    		depth = 1
    		currentNode = self.getRoot()
    		while currentNode.getNext(node) is not None:
    			currentNode = currentNode.getNext(node)
    			depth += 1
    		node.setAxis(depth % self.getDim())
    		currentNode.setNext(node)

    def findNode(self,node):
    	if self.getRoot() is None:
    		raise ValueError("Tree is empty")
    	else:
    		currentNode = self.getRoot()
    		while currentNode.getData() != node.getData():
    			if currentNode.getNext(node) is None:
    				raise ValueError("Value not found!")
    			else:
    				currentNode = currentNode.getNext(node)
    		return currentNode

    def nnSearch(self,searchNode,startNode,bestNode=None,bestDistance=float("Inf")):
    	currentNode = startNode
    	
    	# get to the leaf
    	while currentNode.getNext(searchNode) is not None:
    		currentNode = currentNode.getNext(searchNode)

    	# check if leaf is better than parent
    	if self.d(currentNode,searchNode) < bestDistance:
    		bestDistance = self.d(currentNode,searchNode)
   	 	
   	 	#recursively traverse
       	while currentNode != startNode:
    		currentNode = curretNode.getParent()
    		if self.d(currentNode,searchNode) < bestDistance:
    			bestNode = currentNode
    			bestDistance = self.d(bestNode,searchNode)
    		if self.dAbs(searchNode,currentNode) < bestDistance:
    			# if we cross the hyperplane, get the new best from the next tree
    			newBest = self.nnSearch(searchNode,currentNode.getOpposite(),bestNode,bestDistance)
    			if d(newBest,searchNode) <= bestDistance:
    				bestNode = newBest

    	return bestNode

    def getNearestNeightbor(self,searchNode):
    	if self.getRoot() is None:
    		raise ValueError("kdTree is empty!")
    	else:
    		return self.nnSearch(searchNode,self.getRoot())



# Tests for kdNode 
# if __name__ == '__main__':
# 	x = Node()
# 	x.setData([5])
# 	x.setAxis(0)
# 	y = Node()
# 	y.setAxis(0)
# 	y.setData([3])
# 	x.setNext(y)
# 	print(y.getParent().getData())
