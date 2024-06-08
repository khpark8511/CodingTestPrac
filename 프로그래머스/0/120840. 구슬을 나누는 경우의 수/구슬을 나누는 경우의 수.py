from functools import reduce
def solution(balls, share):
    if balls - share == 0: return 1 
    else: 
        up = reduce(lambda x,y:x*y, [i for i in range(balls,share, -1)])
        down = reduce(lambda x,y:x*y, [i for i in range(balls-share,0,-1)])
        return int(up/down)