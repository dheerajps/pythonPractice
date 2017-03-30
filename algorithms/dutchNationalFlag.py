""" DUTCH NATIONAL FLAG PROBLEM 
    SORT IN PLACE WITH O(N) 
    You should make only pass of the array of integers
    Variations: Red White and Blue
    Partition based on given pivots etc """

""" 1. If number pointed by reader is 0, swap with number at low index and move low one step ahead.
    2. If number pointed by reader is 1, do nothing, increment reader.
    3. If number pointed by reader is 2. swap it with high index and decrement high.
"""

def dutchNationalFlag(array):

    low = 0
    reader = 0
    high = len(array) -1
    
    while (reader < high):

        if(array[reader] == 0):
            
            array[reader],array[low] = array[low],array[reader]  #swap the values
            low+=1
            reader+=1
        
        elif(array[reader] == 1):

            reader +=1

        else:

            array[reader],array[high] = array[high],array[reader]
            high -=1

    print "Array after sorted in place and grouped together is ",array
    return

inputArray = [0,1,1,0,2,2,2,1,0,2,1,0,1,2,0,2,0,1,1]
dutchNationalFlag(inputArray)
