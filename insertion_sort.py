###  Insertion Sort  ###

def insertionSort(A):
    for j in range(1,len(A)):
        k = A[j]
        i = j-1
        while i >= 0 and A[i] > k:
            A[i+1] = A[i]
            i=i-1
            A[i+1] = k
    return A

A = [1,3,2,8,12,1000,44,999,0]
print(insertionSort(A))
