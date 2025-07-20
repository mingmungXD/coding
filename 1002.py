import math

def turret (x1, y1, r1, x2, y2, r2):
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    if d == 0 and r1 == r2:
        return -1
    
    elif d == abs(r1 - r2) or d == r1 + r2:
        return 1
    
    elif abs(r1 - r2) < d < r1 + r2:
        return 2
    
    else:
        return 0
    
T = int (input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    print(turret(x1, y1, r1, x2, y2, r2))