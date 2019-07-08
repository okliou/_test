class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        d = dict()
        for i, v in enumerate(numbers):
            if target - v in d:
                return [d[target - v] + 1, i + 1]
            d[v] = i

    def twoSum1(self, numbers: list, target: int) -> list:
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s > target:
                r -= 1
            else:
                l += 1


if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))
