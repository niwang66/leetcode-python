class Solution:
    def climbStairs(self, n: int) -> int:
        if n<= 2:
            return n
        a, b = 1, 2
        i = 3
        while (i <= n):
            a,  b = b, a+b
            i += 1
        return b

if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(8))