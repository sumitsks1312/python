s = "eceba"

def longest_substring(s):
    
    seen = {}
    l = 0
    max_len = 0
    
    for r in range(len(s)):
        
        if s[r] in seen:
            seen[s[r]] += 1
        else:
            seen[s[r]] = 1
            
        while len(seen) > 2:
            
            seen[s[l]] -= 1
            
            if seen[s[l]] == 0:
                del seen[s[l]]
            l += 1
        
        max_len = max(max_len, r - l + 1)
    
    return max_len
    
print(longest_substring(s))


# Time Complexity O(n)
# iterate through the array exactly once with the r pointer.

# Space Complexity O(1)
# The space used by the dictionary is proportional to the number of distinct characters allowed k. 
# In this case, since k = 2, the space is O(1).

