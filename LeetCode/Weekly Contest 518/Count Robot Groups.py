class Solution:
    def countGroups(self, position: list[int], speed: list[int], distance: int) -> int:
        n = len(speed)
        ans = n

        mn = speed[-1]

        for i in range(n - 2, -1, -1):
            if mn < speed[i] or position[i + 1] - position[i] <= distance:
                ans -= 1

            else:
                mn = speed[i]

        return ans