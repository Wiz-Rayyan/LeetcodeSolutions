#in original 2sum v can sort it and use this. though timecomplexity then would bcm n**2 and more
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1 #sollution: two pointer method.
        while l<r:
            Sum = numbers[l] + numbers[r]
            if Sum < target:
                l+=1
            elif Sum > target:
                r-=1
            else:
                return[l+1, r+1] #index considered from 1
        return []



