#From a given list of integers, find the highest product possible from three of the integers

#Input Array should always have at least 3 integers
#Can have negative and positive
#O(Nlog(N)) time and O(1) space
#This works fine for smaller arrays in O(nlogn)


def getMaxProductOfThree(inputArray):

    sortedArray = sorted(inputArray)

    length = len(sortedArray)

    firstCandidate = sortedArray[length -1]*sortedArray[length-2]*sortedArray[length-3]

    secondCandidate = sortedArray[0]*sortedArray[1]*sortedArray[length-1]

    maxProduct = max(firstCandidate,secondCandidate)

    return maxProduct


inputArray = [ -8,-3, -5, 2, 8,9, 1,2,4, 11, 2,33,1]
print " Input Array is ", inputArray
maxProduct = getMaxProductOfThree(inputArray)
print " The maximum possible product of 3 integers is ",maxProduct
