# same as highestProduct.py
# but find the maximum product possible by three numbers in an array without sorting it

#so O(N) must be time requirements

def getMaxProductOfThreeNumbers(array):

    import sys
#Max product can be 3 maximum numbers or 2 minimum numbers and 1 max
    firstMax = -sys.maxsize-1
    secondMax = -sys.maxsize-1
    thirdMax = -sys.maxsize-1

    firstMin = sys.maxsize
    secondMin = sys.maxsize

    i=0
#loop throught the array and keep updating the values
    while i < len(array):

        if(array[i]>firstMax):

            thirdMax = secondMax
            secondMax = firstMax
            firstMax = array[i]
        
        elif(array[i]>secondMax):

            thirdMax = secondMax
            secondMax = array[i]

        elif(array[i]>thirdMax):

            thirdMax = array[i]
        
        if(array[i]<firstMin):

            secondMin = firstMin
            firstMin = array[i]

        elif(array[i] < secondMin):

            secondMin = array[i]

        i+=1
#find the maximum possible product and return it
    return max(firstMin*secondMin*firstMax , firstMax*secondMax*thirdMax)


inputArray = [-1,-7,-8,3,-1,-5,2,3,8,9]
print " The input array is ",inputArray
maxProduct = getMaxProductOfThreeNumbers(inputArray)
print " The max product from 3 numbers(using O(n) time) is ",maxProduct

