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
    
# neetcode
class Solution(object):
    def containsDuplicate(self, nums):
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    

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
        # my solution
        for i, n in enumerate(nums):
            m = target - n
            if m in nums[i+1:]:
                # if there is duplicate
                if m == n:
                    return [nums.index(n), nums.index(m, nums.index(n) + 1)]
                else:
                    return [nums.index(n), nums.index(m)]
        
        # this solution is more efficient since it only looks for the difference in the hashmap O(n) rather than checking through the nums array based on the current number in the array O(n^2) 
        prevMap = {} # val : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i


# 1929. CONCATENATION OF ARRAY
class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # my solution
        return nums + nums
    
        # what if the interviewer wants to expand the concatenation to 3n?
        ans = []
        for i in range(3):
            for n in nums:
                ans.append(n)
        return ans

    
# 146. LRU CACHE [MEDIUM]
# my solution did not work
# main problem: I only know how to implement basic dictionary and I didn't first figure out how to structure how the data is being handled
# I managed to figure out the capacity and the dictionary keys, values but not the LRU and MRU
# according to neetcode, we'd have to use node pointers to determine whether the key is LRU or MRU
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.d = {} # key : value
        self.c = capacity
        self.mru = 0 # key
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        self.mru = key
        # if the key exists, return the key
        if key in self.d:
            return self.d.get(key)
        # else return -1
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # make sure the length of d does not exceed the capacity
        if len(self.d) < self.c:
            self.d[key] = value
            self.mru = key
        # if it exceeds, take out the LRU then add in the new key
        else:
            if self.mru in self.d.keys():
                # pop the element that is not self.u
                if self.c > 1:
                    for k in self.d.items():
                        if k[0] != self.mru:
                            a = k[0]
                else:
                    for k in self.d.items():
                        a = k[0]
                self.d.pop(a)
            else:
                # pop the first element in the dictionary O(1)
                for k, h in self.d.items():
                    self.d.pop(k)
                    break
                # self.d.pop(next(iter(self.d)))
            # then add in the new key
            self.d[key] = value
            print(self.d.keys())

# neetcode solution
