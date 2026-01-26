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


# Time Complexity O(n)
# iterate through the array exactly once with the r pointer.

# Space Complexity O(1)
# only using two integer variables (l and max_len) regardless of how large the input array is
