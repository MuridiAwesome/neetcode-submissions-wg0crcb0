class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        group_nums = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in group_nums:
                return [group_nums[diff], i]
            group_nums[nums[i]] = i
