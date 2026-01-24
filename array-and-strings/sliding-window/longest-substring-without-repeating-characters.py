s="abcabcbb"

def longest_substring(s):
    
    seen = set()
    l = 0
    max_len = 0
    
    for r in range(len(s)):
        
        while s[r] in seen:
            seen.remove(s[l])
            l += 1
            
        seen.add(s[r])
        max_len = max(max_len, r - l + 1)

    return max_len
    
print(longest_substring(s))


# Time Complexity O(n)
# The right pointer r moves from 0 → n-1 once
# The left pointer l also moves from 0 → n-1 once
# total operations are proportional to 2n

# Space Complexity O(n)
# size = n
# No additional arrays or maps
