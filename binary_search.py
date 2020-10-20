###  Binary Search  ###



def binSearch(L,item):
    low = 0
    high = len(L)-1
    found = False
    while low <= high and not found:
        midpoint = (first + last)//2
        if L[midpoint] == item:
            found = True
        elif item < L[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return found
## If the list is sorted, the binary search is faster than linear search
## example: searching for a word in the dictionary.

##Complexity:  T(n) = Big_O( log(n) )

## Worst case: Thea( log(n) )
## Best case: Theta( 1 )
