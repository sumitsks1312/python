prices = [7,1,5,3,6,4]

def best_time_to_buy_stock(prices):
    
    lowest = prices[0]
    profit = 0
    
    for price in prices:
        lowest = min(lowest, price)
        diff = price - lowest
        profit = max(profit, diff)
            
    return profit
    
    
print(best_time_to_buy_stock(prices))

# Time Complexity O(n)
# Single pass through the array

# Space Complexity O(1)
# Only a few variables: lowest, profit, diff
# No additional arrays or maps