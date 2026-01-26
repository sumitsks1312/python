nums = [-1, 2, 1, 2, 1]
target = 1

def three_sum_closest(nums, target):
    
    nums.sort()
    closest = nums[0]+nums[1]+nums[2]
    
    for i in range(len(nums)-2):
        
        l = i + 1
        r = len(nums) - 1
        
        while l < r:
            
            s = nums[i] + nums[l] + nums[r]
            
            if abs(s - target) < abs(closest - target):
                closest = s
            
            
            if s < target:
                l += 1  
            elif s > target:
                r -= 1
            else:
                return s
                
    return closest

print(three_sum_closest(nums, target))



# Time Complexity O(n2)
# Sorting: Takes O(n log n).
# Nested Loops: The outer loop runs n times, and the inner while loop (two-pointer scan) also runs up to n times for each outer iteration
# This results in On2

# Space Complexity O(n)
# Your variables (l, r, s, closest) take constant O(1) space.
# However, Python's sort() (Timsort) requires O(n) auxiliary space in the worst case.

