# 217. CONTAINS DUPLICATE
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # if len(set(nums)) != len(nums):
        #     return True
        # else:
        #     return False
        return True if len(set(nums)) != len(nums) else False
    

# 242. VALID ANAGRAM
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return True if sorted(s) == sorted(t) else False   


# 1. TWO SUM 
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, n in enumerate(nums):
            m = target - n
            if m in nums[i+1:]:
                # if there is duplicate
                if m == n:
                    return [nums.index(n), nums.index(m, nums.index(n) + 1)]
                else:
                    return [nums.index(n), nums.index(m)]