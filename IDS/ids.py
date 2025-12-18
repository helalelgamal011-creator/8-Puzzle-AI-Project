from common import GOAL_STATE,get_neighbors,print_puzzle

def ids(start):
    depth=0
    while True:
        res=dls(start,depth)
        if res: return res
        depth+=1

def dls(state,limit,path=None,visited=None):
    if path is None: path=[state]
    if visited is None: visited=set()
    if state==GOAL_STATE: return path
    if limit<=0: return None
    visited.add(state)
    for n in get_neighbors(state):
        if n not in visited:
            res=dls(n,limit-1,path+[n],visited.copy())
            if res: return res

if __name__=="__main__":
    start=(1,2,3,4,0,6,7,5,8)
    path=ids(start)
    for s in path:
        print_puzzle(s)
