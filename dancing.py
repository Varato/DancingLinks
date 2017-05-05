from base import *

O_seq=[]

def cover_column(column_header):
	# covers the column header
	column_header.R.L = column_header.L
	column_header.L.R = column_header.R

	i = column_header.D
	while i is not column_header:
		j = i.R
		while j is not i:
			j.D.U = j.U
			j.U.D = j.D
			j.C.S -= 1
			j = j.R
		i = i.D


def uncover_column(column_header):
	# uncovers the column header
	i = column_header.U
	while i is not column_header:
		j = i.L
		while j is not i:
			j.D.U = j
			j.U.D = j
			j.C.S += 1
			j = j.L
		i = i.U
	column_header.R.L = column_header
	column_header.L.R = column_header



def search(root):
	if root.R is root:
		for O in O_seq:
			solution = [O.C.N]
			node = O.R
			while node is not O:
				solution.append(node.C.N)
				node = node.R
			print(solution)
		return 0

	c = root.R
	cover_column(c)
	r = c.D
	while r is not c:
		O_seq.append(r)
		j = r.R
		while j is not r:
			cover_column(j.C)
			j = j.R
		search(root)
		r = O_seq.pop()
		c = r.C
		j = r.L
		while j is not r:
			uncover_column(j.C)
			j = j.L
		r = r.D
	uncover_column(c)
	return 1



if __name__ == "__main__":
    A = np.array([[0,0,1,0,1,1,0],
                  [1,0,0,1,0,0,1],
                  [0,1,1,0,0,1,0],
                  [1,0,0,1,0,0,0],
                  [0,1,0,0,0,0,1],
                  [0,0,0,1,1,0,1]])

    root = mat2linklist(A,string.ascii_uppercase[:7])
    search(root)



    # a=root.R
    # print(root.R.R.R.R.S)
    # cover_column(a)
    # print(root.R.R.R.S)
    # uncover_column(a)
    # print(root.R.N)
    # print(root.R.R.R.R.S)

