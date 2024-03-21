class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i : i + k] = reversed(a[i : i + k])
        return "".join(a)

# Test the function
solution = Solution()
print(solution.reverseStr("abcdefg", 2)
print(solution.reverseStr("abcd", 2)

# Time: O(N) - Linear - where N is the size of s. We build a helper array, plus reverse about half the characters in s.
# Space: O(N) - Linear
