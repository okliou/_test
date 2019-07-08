def twoSum(nums: list, target: int) -> list:
    for i, k in enumerate(nums):
        for b, a in enumerate(nums):
            if i == b:
                continue
            elif k + a == target:
                return [i, b]


def twoSum2(nums: list, target: int) -> list:
    a = {}
    for i, k in enumerate(nums):
        if k in a:
            return [a[k], i]
        else:
            a[target - k] = i


if __name__ == '__main__':
    print(twoSum2([2, 7, 11, 15], 9))
