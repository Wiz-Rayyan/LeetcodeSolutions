class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0] #what if first element is max
        summing = 0
        for n in nums:
            if summing < 0:
             summing = 0
            summing +=n
            maxsum = max(maxsum, summing)
        return maxsum
