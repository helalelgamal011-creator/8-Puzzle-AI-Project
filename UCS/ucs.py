import heapq
from common import GOAL_STATE,get_neighbors,print_puzzle

def ucs(start):
    heap=[(0,start,[start])]
    visited=set()
    while heap:
        cost,state,path=heapq.heappop(heap)
        if state==GOAL_STATE:
            return path
        if state in visited:
            continue
        visited.add(state)
        for n in get_neighbors(state):
            if n not in visited:
                heapq.heappush(heap,(cost+1,n,path+[n]))

if __name__=="__main__":
    start=(1,2,3,4,0,6,7,5,8)
    path=ucs(start)
    for s in path:
        print_puzzle(s)
