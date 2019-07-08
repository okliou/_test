class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        a = 0
        for i in nums:
            if i != val:
                nums[a] = i
                a += 1
        print(nums)
        return a

    def removeElement1(self, nums: list, val: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] == val:
                nums[l], nums[r], r = nums[r], nums[l], r-1
                print(nums)
            else:
                l += 1
        return l


if __name__ == '__main__':
    print(Solution().removeElement1([3, 2, 2, 3], 3))
