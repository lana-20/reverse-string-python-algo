class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def in_place_reverse(s, start, end):
            left, right = start, end
            while left < right:
                s[left], s[right] = s[right], s[left]
                left, right = left + 1, right -1
        
        in_place_reverse(s, 0, len(s)-1)

        i = j = 0
        while j <= len(s):
            if j == len(s) or s[j] == " ":
                in_place_reverse(s, i, j - 1)
                i = j + 1
            j += 1

# Test the function
solution = Solution()
print(solution.reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"])
print(solution.reverseWords(["a"])

# Time: O(n) - Linear
# Space: O(n) - Linear
