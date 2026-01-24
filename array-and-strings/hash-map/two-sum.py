nums = [2,11,7,15]
target = 9


def two_sum(nums, target):
    
    seen = {}

    for i, num in enumerate(nums):
    
        diff = target - num
    
        if diff in seen:
            return [seen[diff], i]
    
        seen[num] = i
        print(seen)  
        
    return None
            
      
print(two_sum(nums, target))


# Time Complexity O(n)

# Space Complexity O(n)