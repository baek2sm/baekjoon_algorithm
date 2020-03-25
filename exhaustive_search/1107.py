import sys


def search(n, disabled_button):
    result = abs(n - 100)
    for i in range(0, 1000001):
        is_possible = True
        for j in str(i):
            if j in disabled_button:
                is_possible = False
                break
        if is_possible:
            result = min(result, abs(n - i) + len(str(i)))
    return result


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    disabled_button = set(sys.stdin.readline().split())
    answer = search(n, disabled_button)
    print(answer)