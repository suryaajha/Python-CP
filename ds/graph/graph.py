from collections import defaultdict
from collections import deque

class Graph:
    def __init__(self, vertices, edges, is_directed = True):
        self.adj_list =  defaultdict(list)
        for u, v, w in edges:
            self.adj_list[u].append([v, w])
        if not is_directed:
            for u, v, w in edges:
                self.adj_list[v].append([u, w])

    def __repr__(self):
        for v, neigbours in self.adj_list.items():
            print(v, end=' -> ')
            print(neigbours)
        return ''

    def bfs(self, start_node):
        queue = deque()
        queue.append(start_node)
        parent = {start_node: None}
        while queue:
            next_queue = deque()
            while queue:
                poped = queue.popleft()
                print(poped)
                for neigbour in self.adj_list[poped]:
                    if neigbour[0] not in parent:
                        parent[neigbour[0]] = poped
                        next_queue.append(neigbour[0])
            queue = next_queue
        return parent

    def shortest_path(self, start_node, end_node):
        parent = self.bfs(start_node)
        current_node = end_node
        stk = []
        stk.append(end_node)
        while current_node:
            stk.append(parent[current_node])
            current_node = parent[current_node]
        while stk:
            print(stk.pop(), '->', end='')
        print('END')

    def dfs(self, start_node):
        def visit(node):
            print(node)

        def dfs_helper(graph, parent, start_node, visit):
            for neigbour in graph[start_node]:
                if neigbour[0] not in parent:
                    parent[neigbour[0]] = start_node
                    dfs_helper(graph, parent, neigbour[0], visit)
            visit(start_node)

        parent = {}
        parent[start_node] = None

        dfs_helper(self.adj_list, parent, start_node, visit)

    def dfs_iterative(self, start_node):
        stk = []
        stk.append(start_node)
        parent = {start_node: None}
        while stk:
            poped = stk.pop()
            for neigbour in self.adj_list[poped]:
                if neigbour[0] not in parent:
                    parent[neigbour[0]] = poped
                    stk.append(neigbour[0])
            print(poped)

def main():
    # https://algocoding.files.wordpress.com/2014/08/graph2.png
    g = Graph([0, 1, 2,4,5,6,7],[[0,1,1],[0,2,1],[0,3,1],[3,2,1],[3,4,1],[4,1,0],[1,5,1],[1,6,1],[6,4,1]], True)
    g.dfs_iterative(0)
    print(g)


if __name__ == '__main__':
    main()
