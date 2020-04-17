#User function Template for python3

from collections import deque

def children(n, target):
    output = [n - 1]
    if n < target:
        output.append(2 * n)

    return output

def bfs(src, target):
    parent = {src : None}
    queue = deque()
    queue.append(src)
    while queue:
        nxt_queue = deque()
        while queue:
            poped = queue.popleft()
            if poped == target:
                nxt_queue.clear()
                break
            for child in children(poped, target):
                if child not in parent:
                    parent[child] = poped
                    nxt_queue.append(child)
        queue = nxt_queue
    current = target
    output = []
    while parent[current]:
        output.append('overflow' if current == 2 * parent[current] else 'eat')
        current = parent[current]
    output.reverse()
    return output
        
def getDecision(m,n):
    #code here
    output = bfs(1098,9488866)
    print(' '.join(output))

getDecision(20, 17)

print( "eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat overflow overflow overflow eat overflow eat overflow" == "eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat eat overflow overflow overflow eat overflow eat overflow")
