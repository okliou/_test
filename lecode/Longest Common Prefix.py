class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        a = zip(*strs)
        s = ''
        for i in a:
            if len(set(i)) != 1:
                break
            s += i[0]
        return s


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
