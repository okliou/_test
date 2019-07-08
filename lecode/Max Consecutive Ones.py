class Solution:
    def findMaxConsecutiveOnes(self, nums: list) -> int:
        m = 0
        new = 0
        for i in nums:
            if i != 1:
                m = max(m, new)
                print(m)
                new = 0
                continue
            new += 1
        m = max(m, new)
        return m


if __name__ == '__main__':
    print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
