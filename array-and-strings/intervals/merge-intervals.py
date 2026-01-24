intervals = [[1,3],[2,6],[8,10],[15,18]]

def merge_intervals(intervals):
    
    sorted_intervals = sorted(interval for interval in intervals)
    
    res = [sorted_intervals[0]]
    
    for i in range(1,len(sorted_intervals)):
        
        current = sorted_intervals[i]
        last = res[-1]
        
        if current[0] < last[1]:
            last[1] = max(current[1], last[1])
        else:
            res.append(sorted_intervals[i])
        
        print(res)
        
    return res
    

print(merge_intervals(intervals))


# Time Complexity O(n log n)
# Sorting n intervals → O(n log n)
# Single pass over n intervals → O(n)

# Space Complexity O(n)
# sorted_intervals → creates a new list of length n → O(n)
# res → in worst case (no overlapping intervals) → stores all n intervals → O(n)