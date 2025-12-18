import heapq
from common import GOAL_STATE,get_neighbors,manhattan,print_puzzle

def a_star(start):
    heap=[(manhattan(start),0,start,[start])]
    visited=set()
    while heap:
        f,g,state,path=heapq.heappop(heap)
        if state==GOAL_STATE:
            return path
        if state in visited:
            continue
        visited.add(state)
        for n in get_neighbors(state):
            if n not in visited:
                new_g=g+1
                heapq.heappush(heap,(new_g+manhattan(n),new_g,n,path+[n]))

if __name__=="__main__":
    start=(1,2,3,4,0,6,7,5,8)
    path=a_star(start)
    for s in path:
        print_puzzle(s)
