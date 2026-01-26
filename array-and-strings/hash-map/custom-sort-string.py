order = "cba"
s = "abcd"

def custom_sort(order, s):
    
    priority = {ch: i for i, ch in enumerate(order)}
    
    sorted_s = sorted(s, key=lambda ch: priority.get(ch, len(order)))
    
    return ''.join(sorted_s)
        

print(custom_sort(order, s))

# Time Complexity O(n + m log m)
# Python’s Timsort algorithm takes O(m log m)


# Space Complexity O(n + m)
# priority map stores n characters
# sorted() function creates a new list of the characters in s
