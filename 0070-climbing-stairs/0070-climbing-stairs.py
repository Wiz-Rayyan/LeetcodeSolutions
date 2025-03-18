class Solution:
    def climbStairs(self, n: int) -> int:
        fn1, fn2 = 1, 1
        for i in range(n-1):
            # yeah fabonnachi happening. 
            temp = fn2
            fn2 = fn2 + fn1
            fn1 = temp
        return fn2