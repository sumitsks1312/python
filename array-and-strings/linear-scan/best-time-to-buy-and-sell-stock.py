prices = [7,1,5,3,6,4]

def best_time_to_buy_stock(prices):
    
    lowest = prices[0]
    profit = 0
    
    for price in prices:
        lowest = min(lowest, price)
        diff = price - lowest
        if diff > profit:
            profit = diff
            
    return profit
    
    
    
print(best_time_to_buy_stock(prices))