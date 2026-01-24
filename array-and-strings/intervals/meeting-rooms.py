intervals = [(0,30),(5,10),(15,20)]

def meeting_room(intervals):
    
    sorted_intervals = sorted(intervals, key=lambda interval: interval[0])
    
    for i in range(1,len(sorted_intervals)):
        if sorted_intervals[i][0] < sorted_intervals[i-1][1]:
            return False
    
    return True
    

print(meeting_room(intervals))


# Time Complexity O(n log n)
# Sorting takes O(n log n)
# Then we loop once over all intervals → O(n)

# Space Complexity O(1)
# Extra variables: sorted_intervals, loop variables → O(1) extra
# No extra hash maps or sets