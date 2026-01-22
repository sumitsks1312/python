strs = ["eat","tea","tan","ate","nat","bat"]

def group_anagram(strs):
    
    anagram = {}
    
    for word in strs:
        key = ''.join(sorted(word))
        if key in anagram:
            anagram[key].append(word)
        else:
            anagram[key] = [word]
            
    return list(anagram.values())

print(group_anagram(strs))
