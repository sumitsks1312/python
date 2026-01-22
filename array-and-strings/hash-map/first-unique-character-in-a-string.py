s = "leetcode"

def unique_character(s):
    
    freq = {}
    
    for ch in s:
        freq[ch] = freq.get(ch,0) + 1
    
    for ch in s:
        if freq[ch] == 1:
            return ch
    
    return None

print(unique_character(s))
