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


# Time Complexity O(n * k log k)
# n = number of strings, k = average length of a string
# Sorting each word takes O(k log k)
# You do this for all n words

# Space Complexity O(n * k)
# Keys: sorted versions of words → up to n keys of length k
