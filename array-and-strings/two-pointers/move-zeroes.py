nums = [0,1,0,3,12]

def move_zeroes(nums):
    
    i = 0
    
    for j in range(1,len(nums)):

        if nums[j] != 0 :
            nums[j] , nums[i] = nums[i], nums[j]
            i += 1
    
    return nums
    
print(move_zeroes(nums))
