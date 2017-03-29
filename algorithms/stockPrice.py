"""Best profit you can make from 1 purchase and 1 sale
so you need to find the maximum difference possible from a given array of numbers

constraints:
can have negative value for profit
must buy before selling
O(n) for time and O(1) for space
"""

#vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
def getMaxProfitValue(priceArray):
    if len(priceArray) <2:
        print "Usage Error:-> there must be at least 2 prices to get a profit. Check input"

    minimumPrice = priceArray[0]
    maxProfit = priceArray[1] - priceArray[0] # Here I am initializing it to a first possible value of profit instead of giving it to 0

    for index,currentPrice in enumerate(priceArray):

        if index == 0: #No need to compute anything for the first element as we need at least two prices to perform the calculation
            continue


        profitCandidate = currentPrice - minimumPrice

        maxProfit = max(maxProfit, profitCandidate)

        minimumPrice = min(minimumPrice, currentPrice)

    return maxProfit

profit=getMaxProfitValue([-1,-2,0,2,-1,5,9,3,5,-1])
print "Profit from this price list is: ",profit

    
