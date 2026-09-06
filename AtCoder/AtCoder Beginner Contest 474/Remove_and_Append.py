import sys
input = sys.stdin.readline

def solve():
    n, q = map(int, input().split())
    p = list(map(int, input().split()))

    a = [int(input()) for _ in range(q)]

    pos = [0] * (n + 1)

    for i in range(n):
        pos[p[i]] = i

    for i in range(q):
        x = a[i]
        pos[x] = n + i

    ans = sorted(range(1, n + 1), key=lambda x: pos[x])

    print(*ans)

solve()