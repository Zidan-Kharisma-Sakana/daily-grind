from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = set()
        for idx in range(len(nums)):
            d.add(nums[idx])
        for idx in range(len(nums)):
            counterpart = target - nums[idx]
            if counterpart in d:
                for i in range(len(nums)):
                    if nums[i] + nums[idx] == target and i != idx:
                        return [idx, i]