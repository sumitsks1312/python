nums = [1,4,3,2]

def array_partition(nums):
    
    nums.sort()
    total = 0
    
    for i in range(0, len(nums), 2):
        total += nums[i]
        
    return total

print(array_partition(nums))


# Time Complexity O(n log n)
# Sorting n intervals → O(n log n)

# Space Complexity O(1)
# .sort() sorts the list in-place
