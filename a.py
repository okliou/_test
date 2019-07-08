def slidingwindow(nums: list, k: int) -> list:
    if not nums: return []
    window, res = [], []
    for i, x in enumerate(nums):
        if i >= k and window[0] <= i - k:
            window.pop(0)
        while window and nums[window[-1]] <= x:
            window.pop()
        window.append(i)
        if i >= k - 1:
            res.append(nums[window[0]])
            enumerate
    return res


if __name__ == '__main__':
    print(slidingwindow([1, 2, 3, 1, 5, 2, 6], 3))
