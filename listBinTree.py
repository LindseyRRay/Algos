def Tree(r):
	return [r, [],[]]

def insert(root, newBranch, direction='left'):
	pos = 1
	if direction == 'right':
		pos = 2


	t = root.pop(pos)
	if len(t) >= 1:
		root.insert(pos,[newBranch, t, []])
	else:
		root.insert(pos,[newBranch, [], []])
	return root


def getRoot(root):
	return root[0]

def getChild(root, direction='left'):
	pos = 1
	if direction == 'right':
		pos = 2
	return root[pos]

def buildTree():
	newTree=Tree('a')
	insert(newTree, 'b')
	insert(newTree[1], 'd')
	insert(newTree, 'c', direction='right')
	insert(newTree[2], 'f', direction='right')
	insert(newTree[2], 'e')
	print(newTree)

if __name__ == '__main__':
	buildTree()