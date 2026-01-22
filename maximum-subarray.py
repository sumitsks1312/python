nums = [-2,1,-3,4,-1,2,1,-5,4]

def maximum_subarray(nums):
    
    current_sum = nums[0]
    max_sum = nums[0]
    
    for num in nums[1:]:
        
        current_sum = max(num, num+current_sum)
        
        max_sum = max(current_sum, max_sum)
        
    return max_sum
    
    
print(maximum_subarray(nums))
