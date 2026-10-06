class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       max_profit = 0
       
       for i in range(len(prices)):
           if i == 0:
               current_min = prices[i]
               continue    

           if prices[i] > current_min:
               profit = (prices[i] - current_min)
               max_profit = max(profit, max_profit)
           else:
               current_min = prices[i]
       return max_profit        


