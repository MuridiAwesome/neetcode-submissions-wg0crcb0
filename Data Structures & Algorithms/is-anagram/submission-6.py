class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        group_s = {}
        group_t = {}

        for char in s:
            if char not in group_s:
                group_s[char] = 1
            else:
                group_s[char] += 1

        for char in t:
            if char not in group_t:
                group_t[char] = 1
            else:
                group_t[char] += 1

        return group_s == group_t