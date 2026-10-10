#Author: Cristover N. Vidal
#Event: 3rd Lecture Series in Mathematics, Applied Mathematics, and Statistics
#Organizer: Mathematics and Statistics Department of the University of Southeastern Philippines

#The following functions are used in testing correctness of calculations and conjectures.


import math


#---Return the distance between two vertices i and j in C_n(1,2,...,t)
#t,n are parameters to define C_n(1,2,...,t)
#i,j are the vertices in C_n(1,2,...,t) whose distance are in question
#The distance formula used is from: T. BC, S. Dueck, The metric dimension of circulant graphs, Opuscula Math. 45 (2025) 1, 39–51.
#       and A. Borchert, S. Gosselin, The metric dimension of circulant graphs and Cayley hypergraphs, Util. Math. 106 (2018), 125–147.
def circ_dist(t,n,i,j):
    if abs(i-j) < math.ceil(n/2):
        return math.ceil(abs(i-j)/t)
    else:
        return math.ceil((n-abs(i-j))/t)

#Example:
#print(circ_dist(3,11,1,6))



#---Return True if two vertices i and j are adjacent in C_n(1,2,...,t)
#t,n are parameters to define C_n(1,2,...,t)
#i,j are the vertices in C_n(1,2,...,t), tested if ij is an edge in C_n(1,2,...,t)
#The test is derived from the definition of Consecutive Circulant Graphs:
#T. BC, S. Dueck, The metric dimension of circulant graphs, Opuscula Math. 45 (2025) 1, 39–51.
#       and A. Borchert, S. Gosselin, The metric dimension of circulant graphs and Cayley hypergraphs, Util. Math. 106 (2018), 125–147.
def circ_edge_test(t,n,i,j):
    check = False
    for k in range(1,t+1,1):
        if (j-i)%n == k or (i-j)%n == k:
            check = True
            break
    return check

#Example:
#print(circ_edge_test(3,12,1,8))



#---Return the local resolving neighborhood of the edge ij
#t,n are parameters to define C_n(1,2,...,t)
#i,j are the vertices in C_n(1,2,...,t), where ij is assumed to be an edge in C_n(1,2,...,t)
#The enumeration is based on the foundational paper: I. Javaid, H. Benish, M. Murtaza, The fractional local metric dimension of graphs, Contrib. Discrete Math. 19 (2024), no. 3, 163–177.
def circ_luv_one(t,n,i,j):
    A= []
    for w in range(0,n,1):
        if circ_dist(t,n,i,w) != circ_dist(t,n,j,w):
            A.append(w)
    return sorted(A) , len(A)

#Example:
#print(circ_luv_one(3,11,0,2))



#---Return/print all L(i,j) and |L(i,j)| of all edges ij in C_n(1,2,...,t)
#t,n are parameters to define C_n(1,2,...,t)
#The enumeration is based on the foundational paper: I. Javaid, H. Benish, M. Murtaza, The fractional local metric dimension of graphs, Contrib. Discrete Math. 19 (2024), no. 3, 163–177.
def circ_luv_all(t,n):
    for i in range(0,n,1):
        for j in range(0,n,1):
            if circ_edge_test(t,n,i,j) == True:
                Lij = circ_luv_one(t,n,i,j)
                print("L(",i,",",j,") = ",Lij[0],"; ",Lij[1])
        print()

#Example
#circ_luv_all(2,7)






if __name__ == "__main__":
    circ_luv_all(2,7)
