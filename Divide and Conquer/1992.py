## 쿼드트리

import sys

input = sys.stdin.readline

n = int(input()) 
video = [list(input()) for _ in range(n)] 

def divide(x, y, n): 
    ans = [] 
    check = True 
    color = video[x][y] 
    
    for i in range(x, x+n): 
        if not check: 
            break 
        for j in range(y, y+n): 
            if color != video[i][j]: 
                check = False 
                ans.append("(") 
                ans.extend(divide(x, y, n//2)) 
                ans.extend(divide(x, y+n//2, n//2)) 
                ans.extend(divide(x+n//2, y, n//2)) 
                ans.extend(divide(x+n//2, y+n//2, n//2)) 
                ans.append(")") 
                return ans 
    return color 

print("".join(divide(0, 0, n)))