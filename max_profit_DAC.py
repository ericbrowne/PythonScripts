## Divide and Conquer max profit ##

def MSS1(A):
    """For each subarray A[i,j], find the net change and keep the maximum"""
    best = 0
    n = len(A)
    for i in range(0,n):
        for j in range(i,n):
            sum = 0
            for k in range(i, j+1):
                sum += A[k]
            if sum > best:
                best = sum
    return best

# MSS1: complexity: T(n) = Theta( n^3 )


def MSS2(A):
"""Gets rid of the third loop from MSS1"""
    best,ffrom,to = 0,0,-1
    n=len(A)
    for i in range(0,n):
        sum = 0
        for j in range(i,n):
            sum = sum + A[j]
            if sum > best:
                best,ffrom,to = sum, i, j
    return best
# MSS2: complexity : T(n) = Theta( n^2 )




######  The Divide And Conquer Part  ######
def MSSDAC(A, low=0, high=None):
    if high == None:
        high = len(A)-1
    #Base Case
    if low == high:
        if A[low] > 0:
            return A[low]
        else:
            return 0
    #Divide
    mid = (low+high)//2
    #Conquer
    maxLeft = MSSDAC(A,low,mid)
    maxRight = MSSDAC(A,mid+1, high)
    #Combine
    maxLeft2Center = left2Center = 0
    for i in range(mid, low-1, -1):
        left2Center += A[i]
        maxLeft2Center = max(left2Center, maxLeft2Center)
    maxRight2Center = right2Center = 0
    for i in range(mid+1, high+1):
        right2Center += A[i]
        maxRight2Center = max(right2Center, maxRight2Center)
    return max(maxLeft, maxRight, maxLeft2Center+maxRight2Center)


## MSSDAC: complexity: T(n) = 2T(n/2) + n   is in Theta( nlog(n) )
