import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    idx = -1

    for i in range(n):
        if a[i] > b[i]:
            idx = i
            break

    if idx == -1:
        print("No")
        return

    w = [1] * n
    w[idx] = 10**18

    print("Yes")
    print(*w)

solve()