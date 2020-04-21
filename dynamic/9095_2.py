import sys

if __name__ == '__main__':
    t = int(sys.stdin.readline())
    answer_list = [1, 2, 4]

    for i in range(3, 11):
        answer_list.append(sum(answer_list[-3:]))

    for _ in range(t):
        n = int(sys.stdin.readline())
        print(answer_list[n-1])
