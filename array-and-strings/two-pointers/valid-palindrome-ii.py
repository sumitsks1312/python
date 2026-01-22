s = "abcba"

def is_palindrome_after_delete(s):
    
    s = ''.join(c.lower() for c in s if c.isalnum())
    
    def is_palindrome(l, r):
        while l < r:
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        return True
                
    
    l = 0
    r = len(s) - 1
    
    while l < r:
        
        if s[l].lower() == s[r].lower():
            l += 1
            r -= 1
        else:
            return is_palindrome(l+1,r) or is_palindrome(l,r-1)
    
    return True
            
print(is_palindrome_after_delete(s))
    