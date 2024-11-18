

def DFS(graph, node, visited):
    visited[node] = True
    # print(f"graph[{node}] = {graph[node]}")
    print(node, end = " ")
    for neighbor in graph[node]:
        if not visited[neighbor]:
            DFS(graph,neighbor, visited)
    
    

from collections import deque
def BFS(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        # print(f"graph[{node}] = {graph[node]}")
        print(node, end = " ")
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
        

# def DFS(graph, node):




# get input N, M ,V
N, M, V = map(int,input().split())
# graph 초기화:
graph = [[] for _ in range(N+1)]
for i in range(M):
    u, v = map(int, input().split())
    # u, v = u-1, v-1
    graph[u].append(v)
    graph[v].append(u)
    # print(f"after adding {u}, {v} : \n{graph}")
    
# 하나의 정점에서 작은 점부터 방문해야하므로 graph를 sort해야한다.
for i in range(1, len(graph)):
    # print(f"graph[{i}]: before sort: \n {graph[i]}")
    graph[i].sort()
    # print(f"graph[{i}]: after sort: \n {graph[i]}")

visited_dfs = [False] * len(graph)
visited_bfs = [False] * len(graph)

DFS(graph, V, visited_dfs)
print()
BFS(graph, V, visited_bfs)



# print(graph)

