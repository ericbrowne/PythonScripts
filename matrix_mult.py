###  Matrix Multiplication  ###

def mulMatrix(A,B):
    rowA = len(A)
    colA = len(A[0])
    rowB - len(B)
    colB = len(B[0])
    assert colA == rowB
    C = newmatrix(rowA,rowB)

    for i in range(rowA):
        for j in range(colB):
            sum = 0
            for k in range(0,colA):
                sum+= A[i][k]*B[k][j]
            C[i][j] = sum
    return C

## multiplying 2 nxn matrices gives:  T(n) = theta( nsqrt(n) )
## if d is the dimension of a dxd matrix, then T(d) = theta( d^3 )

def newMatrix():
    '''Helper function to mulMatrix'''
