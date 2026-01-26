strs = ["flower","flow","flight"]

def longest_common_prefix(strs):
    
    for i in range(len(strs[0])):
        
        for word in strs:
            if i >= len(word) or word[i] != strs[0][i]:
                return strs[0][:i]
            
    return strs[0]
    
print(longest_common_prefix(strs))

# Time Complexity O(s)
# Where s is the sum of all characters in all strings

# Space Complexity O(1)
