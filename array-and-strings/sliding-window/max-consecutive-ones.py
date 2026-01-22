nums = [1,1,0,0,1,1,1]

def max_consecutive_ones(nums):
    
    l = 0
    max_len = 0
    
    for r in range(len(nums)):
        
        if nums[r] != 1:
            l = r + 1
        else:       
            max_len = max(max_len, r - l + 1)
        
    return max_len
    
print(max_consecutive_ones(nums))