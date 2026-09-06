class Solution:
    def countRotations(self, s: str, k: int) -> int:
        tmp = s + s
        n = len(s)

        ans = 0

        for i in range(n):
            cnt = 0

            for j in range(i, i + n - 1):

                if tmp[j] == tmp[j + 1]:
                    cnt += 1

            if cnt == k:
                ans += 1

        return ans