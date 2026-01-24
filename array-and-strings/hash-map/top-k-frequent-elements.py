nums = [1,2,2,3,3,3]
k = 2

def top_k_elements(nums):
    
    freq = {}
    
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    sorted_num = sorted(freq, key=lambda num:freq[num], reverse=True)
    
    return sorted_num[:2]

print(top_k_elements(nums))



# Time Complexity O(n + m log m)
# n = length of nums, m = number of unique elements
# Building frequency map → O(n)
# Sorting m unique elements → O(m log m)

# Space Complexity O(n)
# Frequency dictionary → O(m)
# Sorted list → O(m)

# Optimize with bucket sort