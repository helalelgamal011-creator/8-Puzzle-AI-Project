from common import GOAL_STATE, get_neighbors, print_puzzle

def dfs(start):
    stack = [(start,[start])]
    visited = set()
    while stack:
        state, path = stack.pop()
        if state==GOAL_STATE:
            return path
        if state in visited:
            continue
        visited.add(state)
        for n in reversed(get_neighbors(state)):
            if n not in visited:
                stack.append((n,path+[n]))

if __name__=="__main__":
    start = (1,2,3,4,0,6,7,5,8)
    path = dfs(start)
    for s in path:
        print_puzzle(s)
