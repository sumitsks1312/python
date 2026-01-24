s = "anagram"
t = "nagaram"

def valid_anagram(s,t):
    
    if len(s) != len(t):
        return False
    
    freq = {}
    
    for ch in s:
        freq[ch] = freq.get(ch,0) + 1
    
    for ch in t:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] < 0:
            return False
    
    return True

print(valid_anagram(s,t))

# Time Complexity O(n)
# First loop over s → O(n)
# Second loop over t → O(n)

# Space Complexity O(n)
# freq stores character counts