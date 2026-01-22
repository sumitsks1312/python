nums = [1,2,3,1]

def contains_duplicate(nums):
    
    freq = {}
    
    for num in nums:
        if num in freq:
            return True
        freq[num] = 1
    
    return False
        

print(contains_duplicate(nums))
