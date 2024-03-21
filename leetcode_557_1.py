class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        l = 0
        for r in range(len(s)):
            if s[r] == " " or r == len(s) - 1:
                temp_l, temp_r = l, r - 1

                if r == len(s) - 1:
                    temp_r = r
                while temp_l < temp_r:
                    s[temp_l], s[temp_r] = s[temp_r], s[temp_l]
                    temp_l += 1
                    temp_r -= 1
                l = r + 1

        return "".join(s)

# Test the function
solution = Solution()
print(solution.reverseWords("Let's take LeetCode contest")
print(solution.reverseWords("Mr Ding")

# Time: O(n) - Linear - where n is the size of s.
# Space: O(1) - Constant
# If we're converting s to a list, technically we are using extra memory O(n). But generally we don't count the output as memory. The list is not necessary; but if we don't use the list, we still end up having to use extra memory by the string manipulation (by taking substrings and then manipulating the entire string). Depending on how you see it, technically we're using extra memory. If you or your interviewer don't consider it a constraint, then space efficiency is O(1) - Constant.
