class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complements = {}
        for x in range(len(nums)):
            if nums[x] in complements:
                return [complements[nums[x]], x]
            else:
                complements[target-nums[x]] = x