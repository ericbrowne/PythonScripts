###  Divide and Conquer Example  ###
### MergeSort: Order( nlog(n) )

#Helper Function: merge, for mergeSort
def merge(A, B):
    out = []
    i,j=0,0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            out.append(A[i])
            i+=1
        else:
            out.append(B[j])
            j+=1
    while i < len(A):
        out.append(A[i])
        i+=1
    while j < len(B):
        out.append(B[j])
        j+=1
    return out


def mergeSort(L):
    print(f"Before the Sort: {L}")
    if len(L) < 2:
        return L[:]
    else:
        mid = len(L)//2
        Left = mergeSort(L[:mid])
        Right = mergeSort(L[mid:])
        return merge(Left,Right)

L = [1,7,4,2,55,89898,0]
print(mergeSort(L))
