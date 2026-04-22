class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        group = {}

        for num in nums:
            if num in group:
                group[num] += 1
            else:
                group[num] = 1
        
        highest = [0, 0]

        for key, value in group.items():
            if value > highest[1]:
                highest[0] = key
                highest[1] = value
        return highest[0]