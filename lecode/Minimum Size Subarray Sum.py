class Solution:
    def minSubArrayLen(self, s: int, nums: list) -> int:
        total = left = 0
        result = len(nums)
        for right, n in enumerate(nums):
            total += n
            while total >= s:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
        return result if result <= len(nums) else 0


if __name__ == '__main__':
    print(Solution().minSubArrayLen(3, [1, 1]))
