#BEST TIME TO BUY STOCKS(leetcode)

#main concept is that the buying price should be always less than the selling price 

class Solution:

    def maxProfit(self, prices):
        
        if not prices:
            return 0
    
        ans = 0       #starting with ans = 0    
        
        mini = prices[0]        #minimum price is the value at 0th index and we will traverse accordingly
        
        for i in range(1,len(prices)):      #now traversing through the elements of the list
            
            if prices[i] < mini:            #comparing thee value of price at current index with min 
                
                mini = prices[i]            #and updating the value    
                
            else:
                
                ans = max(ans,prices[i]-mini)   #assigning the value of ans by finding the max of ans&price at current index and mini
                
        return ans                              #in the end returning the ans
