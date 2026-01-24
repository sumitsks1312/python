s = "A man, a plan, a canal: Panama"

def is_palindrome(s):
    
    l = 0
    r = len(s) - 1

    
    while l < r:
        
        while l < r and not s[l].isalnum():
            l += 1
         
        while l < r and not s[r].isalnum():
            r -= 1
        
        if s[l].lower() != s[r].lower():
            return False
        
        l += 1
        r -= 1

    return True

print(is_palindrome(s))


# Time Complexity O(n)
# n = len(s)

# Space Complexity O(1)
# Only l, r and a few temporary variables
# No extra arrays, strings, or hash maps