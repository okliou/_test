class Solution:
    def reverseString(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            print(s[i], s[- i - 1])
            s[i], s[- i - 1] = s[- i - 1], s[i]
            print(s[i], s[- i - 1], '-'*20)

        return s


if __name__ == '__main__':
    print(Solution().reverseString(["H","a","n","n","a","h"]))
