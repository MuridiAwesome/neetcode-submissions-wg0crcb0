class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}

        for index in range(len(nums)):
            diff = target - nums[index]

            if diff in prev_map:
                return [prev_map[diff], index]
            prev_map[nums[index]] = index
        return []