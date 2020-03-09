import sys


def flip(mat, i, j):
    for y in range(i, i+3):
        for x in range(j, j+3):
            mat[y][x] = 1 - mat[y][x]
    return mat


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())

    mat_a = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
    mat_b = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

    answer = 0
    for i in range(n-2):
        for j in range(m-2):
            if mat_a[i][j] != mat_b[i][j]:
                answer += 1
                mat_a = flip(mat_a, i, j)

    if mat_a == mat_b:
        print(answer)
    else:
        print(-1)
