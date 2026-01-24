nums = [1,2,3,1]

def contains_duplicate(nums):
    
    seen = set()
    
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    
    return False
        

print(contains_duplicate(nums))

# Time Complexity O(n)
# You iterate through nums once


# Space Complexity O(n)
# You store every element in freq
