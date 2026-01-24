intervals = [(0, 5), (2, 7), (4, 9), (6, 10)]

def meeting_room_ii(intervals):
    
    starts = sorted(interval[0] for interval in intervals)
    ends = sorted(interval[1] for interval in intervals)
    
    s_ptr = 0
    e_ptr = 0
    rooms = 0
    
    while s_ptr < len(starts):
        
        if starts[s_ptr] < ends[e_ptr]:
            rooms += 1
        else:
            e_ptr += 1
        
        s_ptr += 1
    
    return rooms
    

print(meeting_room_ii(intervals))


# Time Complexity O(n log n)
# Creating starts/end list → O(n)
# Sorting starts/end → O(n log n)
# Two-pointer loop → O(n)

# Space Complexity O(n)
# starts/end list → O(n)
# Other variables → O(1)
