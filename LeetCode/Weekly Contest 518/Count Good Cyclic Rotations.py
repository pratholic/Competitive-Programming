class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n = len(nums)

        tmp = nums + nums

        ans = 0

        pref = [0] * (len(tmp))
        pref[0] = tmp[0]

        for i in range(1, len(tmp)):
            pref[i] = pref[i - 1] + tmp[i]

        i = 0
        j = n - 1

        while i < n:
            sz = j - i + 1
            half = sz // 2

            first = pref[i + half - 1] - (pref[i - 1] if i > 0 else 0) 
            total = pref[j] - (pref[i - 1] if i > 0 else 0)
            later = total - first

            if first > later:
                ans += 1

            i += 1
            j += 1

        return ans