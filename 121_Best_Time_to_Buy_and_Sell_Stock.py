class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # use two pointers one for buy and one for sell
        # buy will be initially set to 0th position
        # sell is set to 1th position 
        # edge case - if only one element return 0 profit. 
        
        # profit = sell - buy
        # if profit is negative, then buy comes sell and sell becomes buy + 1 
        # else make note of max profit and increment sell pointer 

        i = 0
        j = 1
        maxProfit = 0 
        while j<len(prices):
            if prices[j]>prices[i]:
                maxProfit = max(maxProfit, prices[j]-prices[i])
            else:
                i = j 
            j = j + 1 
        return maxProfit

        