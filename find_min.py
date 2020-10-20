### Finding the Minimum in a list ###


def findMin(list):
    #Base Case
    if len(list) == 1:
        return list[0]
    #Recursive case:
    else:
        mid = len(list)//2 #midpoint
        firstHalfList = list[0:mid]
        secondHalfList = list[mid+1:len(list)-1]
        return min(findMin(firstHalfList), findMin(secondHalfList))

        ## Something else needs to be added to this code for it to work!!!
list = [1,2,5,6,4,443,235,0,885,4,234]
print(findMin(list))
