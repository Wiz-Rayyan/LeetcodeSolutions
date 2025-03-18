class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     prevEl = {} # val and index

     for i, n in enumerate(nums):
         diff = target - n
         if diff in prevEl:
            return [prevEl[diff], i]
         prevEl[n] = i
     return
        