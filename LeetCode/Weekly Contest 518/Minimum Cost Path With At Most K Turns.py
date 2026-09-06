from functools import cache

class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        INF = float('inf')

        if m > 1 and n > 1 and k == 0:
            return -1

        def valid(i, j):
            return i >= 0 and i < m and j >= 0 and j < n

        @cache
        def f(i, j, prev_dir, turns_left):
            if i == m - 1 and j == n - 1:
                return grid[i][j]

            ans = INF

            for nd, (dx, dy) in enumerate(dirs):
                nr = dx + i
                nc = dy + j

                if not valid(nr, nc):
                    continue

                new_k = turns_left - (nd != prev_dir)

                if new_k < 0:
                    continue

                ans = min(ans, f(nr, nc, nd, new_k))

            ans += grid[i][j]
            return ans

        return min(f(0, 0, 0, k), f(0, 0, 1, k))