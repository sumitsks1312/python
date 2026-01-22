order = "cba"
s = "abcd"

def custom_sort(order, s):
    
    priority = {ch: i for i, ch in enumerate(order)}
    
    sorted_s = sorted(s, key=lambda ch: priority.get(ch, len(order)))
    
    return ''.join(sorted_s)
        

print(custom_sort(order, s))

