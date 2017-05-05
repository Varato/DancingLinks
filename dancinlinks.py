import numpy as np

class Root:
    def __init__(self):
        self.r=None
        self.l=None
    def R(self):
        return self.r
    def L(self):
        return self.l

class Column:
    def __init__(self):
        self.r=None
        self.l=None
        self.u=None
        self.d=None
        self.s=0
        self.n=""
    def R(self):
        return self.r
    def L(self):
        return self.l
    def U(self):
        return self.u
    def D(self):
        return self.d
    
class Node:
    def __init__(self):
        self.r=None
        self.l=None
        self.u=None
        self.d=None
        self.c=None
    def R(self):
        return self.r
    def L(self):
        return self.l
    def U(self):
        return self.u
    def D(self):
        return self.d
    def C(self):
        return self.c

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
            column_header.n = column_names[j]
        else:
            column_header.n = j
        tmp2 = column_header
        tmp1.r = column_header
        column_header.l = tmp1
        tmp1 = column_header
        column = [None] * r_n
        for i in range(r_n):
            if A[i,j] == 1:
                column_header.s += 1
                node = Node()
                column[i] = node
                node.c = column_header
                tmp2.d = node
                node.u = tmp2
                tmp2 = node
        nodes[j] = column             
        tmp2.d = column_header
        column_header.u = tmp2

    tmp1.r=root
    root.l=tmp1
    
    for i in range(r_n):
        for j in range(c_n):
            if A[i,j] == 1:
                tmp = nodes[j][i]
                # keeps searching the next 1 on the right
                for k in range(1, c_n+1):
                    if A[i, np.mod(j+k, c_n)]==1:
                        node_r = nodes[np.mod(j+k,c_n)][i]
                        tmp.r = node_r
                        node_r.l = tmp
                        tmp = node_r
                break
    return root

if __name__ == "__main__":
    A = np.array([[0,0,1,0,1,1,0],
                  [1,0,0,1,0,0,1],
                  [0,1,1,0,0,1,0],
                  [1,0,0,1,0,0,0],
                  [0,1,0,0,0,0,1],
                  [0,0,0,1,1,0,1]])

    root0 = mat2linklist(A)