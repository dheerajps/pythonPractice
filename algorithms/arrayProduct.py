""" Given a list of integers , and for each index you have to find the product of every integer except the integer at that index """
""" Input : [1,5,7]
    Output : [35, 7, 1]
    Explanation : [5*7, 7*1, 5*1] """
def getProductArray(inputArray):
    
    if len(inputArray)<2:
        print "USAGE ERROR  :-> Need atleast 2 numbers to get product of numbers at other indices"
        
    productArray = [None]*len(inputArray) #initialize an array of same size

    allLeftProducts = 1 #get the product of every element to the left of each index
    index = 0
    for number in enumerate(inputArray):

        productArray[index] = allLeftProducts
        allLeftProducts *= inputArray[index]
        index += 1
    
    index = len(inputArray) -1
    allRightProducts = 1 #get the product of every element to the right of each index
    for number in enumerate(inputArray):

        productArray[index] *= allRightProducts
        allRightProducts *= inputArray[index]
        index -= 1

    return productArray

inputArray = [2,6,1,7,5,3,1]
print "The input array is ",inputArray
productArray = getProductArray(inputArray)
print "The product array as constructed is ",productArray
#O(N) TIME AND O(N) space
