
###  An example of INCREMENTAL DESIGN  ###

def sort(A,n):
    print(f"Before Sort: {A}")
    for i in range(1,n-1):
        key = A[i]
        j = i-1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1]=key
    return A


A =[1,6,7,3,5,8]
print(sort(A,len(A)))
