nums = [2,7,11,15]
target = 9


def two_sum(nums, target):
    
    l = 0
    r = len(nums)-1
    
    while l < r:
        if nums[l]+nums[r] == target:
            return [l, r]
        elif nums[l]+nums[r] < target:
            l += 1
        elif nums[l]+nums[r] > target:
            r -= 1
        
    return None
            
      
print(two_sum(nums, target))
