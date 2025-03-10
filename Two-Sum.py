class Solution(object):
    def twoSum(self, nums, target):
        \\\
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        \\\
        dictionary = dict()

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dictionary:
                return [dictionary[diff], i]
            dictionary[nums[i]] = i
        
