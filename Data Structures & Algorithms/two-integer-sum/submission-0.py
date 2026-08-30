class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value = {}
        for i in range(len(nums)):
            result = target - nums[i]
            if result in value:
                return [value[result], i]
            value[nums[i]] = i
        