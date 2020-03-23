import sys
from collections import deque


def search(path, start, end, max):
    # 이진 탐색으로 이동 가능한 최대 무게 확인
    f, l = 1, max
    result = 0
    while f <= l:
        mid = (f+l)//2
        if check(path, start, end, mid):
            f = mid+1
            result = mid
        else:
            l = mid-1
    return result


def check(path, start, end, cost):
    # 너비 우선 탐색으로 방문 가능여부 확인
    candidate = deque()
    candidate.append(start)
    visited = set()
    while len(candidate) > 0:
        cur = candidate.popleft()
        for t, w in path[cur]:
            if w >= cost and t == end:
                return True
            elif w >= cost and t not in visited:
                candidate.append(t)
                visited.add(t)
    return False


if __name__ == '__main__':
    # 섬의 수와 다리의 수
    n, m = map(int, sys.stdin.readline().split())
    # 경로를 입력받고 시간 복잡도를 낮추기 위해 무게의 max값을 미리 할당
    path = [[] for _ in range(n+1)]
    max = 1
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        path[a].append((b, c))
        path[b].append((a, c))
        if c > max:
            max = c
    # 출발, 도착지
    start, end = map(int, sys.stdin.readline().split())
    # 최대 무게 탐색
    answer = search(path, start, end, max)
    # 결과 출력
    print(answer)