from collections import deque
from common import GOAL_STATE, get_neighbors, print_puzzle

def bfs(start):
    queue = deque([(start,[start])])
    visited = set()
    while queue:
        state,path = queue.popleft()
        if state==GOAL_STATE:
            return path
        if state in visited:
            continue
        visited.add(state)
        for n in get_neighbors(state):
            if n not in visited:
                queue.append((n,path+[n]))

if __name__=="__main__":
    start=(1,2,3,4,0,6,7,5,8)
    path=bfs(start)
    for s in path:
        print_puzzle(s)
