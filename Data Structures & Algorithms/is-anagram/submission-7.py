class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        group_s = {}
        group_t = {}

        for c in s:
            if c not in group_s:
                group_s[c] = 1
            else:
                group_s[c] += 1

        for c in t:
            if c not in group_t:
                group_t[c] = 1
            else:
                group_t[c] += 1

        return group_s == group_t