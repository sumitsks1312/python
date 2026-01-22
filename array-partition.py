nums = [1,4,3,2]

def array_partition(nums):
    
    nums.sort()
    total = 0
    
    for i in range(0, len(nums), 2):
        total += num[i]
        
    return total

print(array_partition(nums))