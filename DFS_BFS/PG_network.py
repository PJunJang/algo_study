# 구현 아이디어: DFS 로 연결된 요소의 개수를 찾아줘야겠다. 백준의 연결요소개수(11724), 단지번호 붙이기(2667) 과 유사한 문제로 보인다.
# 모든 노드를 돌면서 visited 가 아닌 노드일때 DFS로 완전 탐색
#     DFS 를 탈출하면 한개의 네트워크가 완성이므로 cnt +1
#       cnt가 연결 네트워크의 개수이다.

def DFS(computers, node, visited):
    visited[node] = True
    for neighbor in range(len(computers)):
        # print(f"    neighbor: {neighbor} , visited[{neighbor}]: {visited[neighbor]}")
        if computers[node][neighbor] == 1 and not visited[neighbor]:
            DFS(computers, neighbor, visited)

def solution(n, computers):
    #     그래프를 어떻게 정의해줘야 할까?
    #       여기서 graph는 즉 computers 이다.
    visited = [False] * n
    cnt = 0
    for node in range(n):
        # print(f"node: {node}, computers[{node}]: {computers[node]}")
        if not visited[node]:
            DFS(computers, node, visited)
            cnt += 1

        answer = cnt

    return answer
