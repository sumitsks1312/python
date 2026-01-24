nums = [-1,0,1,2,-1,-4]
target = 0


def three_sum(nums, target):
    
    nums.sort()
    res = []
    
    for i in range(len(nums)):
        
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        l = i+1
        r = len(nums) -1
        
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            
            if s == target:
                
                res.append([nums[i] , nums[l] , nums[r]])
                
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                    
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                
                l += 1
                r -= 1
                
            elif s < target:
                l += 1
                
            elif s > target:
                r -= 1
        
        
    return res
            
      
print(three_sum(nums, target))


# Time Complexity O(n^2)
# two nested loops (outer i, inner two-pointer)

# Space Complexity O(1)
# i, l, r, s → constant
# No hash maps, sets, or arrays
