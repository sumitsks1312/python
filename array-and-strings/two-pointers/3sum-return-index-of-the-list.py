nums = [2,2,1,1,1]
target = 4


def three_sum(nums, target):
    
    arr = [(num, i) for i, num in enumerate(nums)]
    arr.sort()
    
    res = []
    
    for i in range(len(arr)):
        
        l = i + 1
        r = len(arr) -1
        
        while l < r:
            
            s = arr[i][0] + arr[l][0] + arr[r][0]
            
            if s == target:
                
                l_idx = [arr[l]]
                while l < r and arr[l][0] == arr[l+1][0]:
                    l += 1
                    l_idx.append(arr[l])
                
                
                r_idx = [arr[r]]
                while l < r and arr[r][0] == arr[r-1][0]:
                    r -= 1
                    r_idx.append(arr[r])
                    
                
                for li in l_idx:
                    for ri in r_idx:
                        res.append([i, li[1], ri[1]])
                    
                
                l += 1
                r -= 1
            
            elif s < target:
                l += 1
            elif s > target:
                r -= 1
                
    return res
            
      
print(three_sum(nums, target))

