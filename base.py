import numpy as np
import string

class Root:
	def __init__(self):
		self.R=None
		self.L=None

class Column:
	def __init__(self):
		self.R=None
		self.L=None
		self.U=None
		self.D=None
		self.S=0
		self.N=""
    
class Node:
	def __init__(self):
		self.R=None
		self.L=None
		self.U=None
		self.D=None
		self.C=None

def mat2linklist(A, column_names=None):
	"""
	A: 0-1 array
	"""
	root = Root()
	tmp1 = root
	r_n,c_n = A.shape 
	nodes = [None] * c_n
	for j in range(c_n):
		column_header = Column()
		if column_names:
			column_header.N = column_names[j]
		else:
			column_header.N = j
		tmp2 = column_header
		tmp1.R = column_header
		column_header.L = tmp1
		tmp1 = column_header
		column = [None] * r_n
		for i in range(r_n):
			if A[i,j] == 1:
				column_header.S += 1
				node = Node()
				column[i] = node
				node.C = column_header
				tmp2.D = node
				node.U = tmp2
				tmp2 = node
		nodes[j] = column             
		tmp2.D = column_header
		column_header.U = tmp2

	tmp1.R=root
	root.L=tmp1
    
	for i in range(r_n):
		for j in range(c_n):
			if A[i,j] == 1:
				tmp = nodes[j][i]
				# keeps searching the next 1 on the right
				for k in range(1, c_n+1):
					if A[i, np.mod(j+k, c_n)]==1:
						node_r = nodes[np.mod(j+k,c_n)][i]
						tmp.R = node_r
						node_r.L = tmp
						tmp = node_r
				break
	return root

