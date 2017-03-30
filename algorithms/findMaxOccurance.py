""" Maximum value K such that array has at-least K elements that are >= K """

def findMax(array):
    
    i=0
    length = len(array)
    frequency = [0]*(length+1)
    while i<length:

        if(array[i] < length):

            frequency[array[i]]+=1

        else:

            frequency[length]+=1
        i+=1

    summation = 0
    i=length
    while i>0:

        summation += frequency[i]

        if(summation >= i):

            return i
        i-=1

inputArray = [900, 2, 901, 3, 1000, 1001,3]
maxVal = findMax(inputArray)
print "The input array is ",inputArray
print "The value is ",maxVal
