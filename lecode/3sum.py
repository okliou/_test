class Solution:
    def threeSum(self, nums: list) -> list:
        if len(nums) < 3:
            return []
        nums.sort()
        print(nums)
        r = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    r.add((v, -v-x, x))
        return list(r)


if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
