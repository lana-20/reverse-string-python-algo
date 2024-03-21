class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        slist = list(s)

        l, r = 0, len(slist) - 1
        while l < r:
            while l < r and slist[l] not in vowels:
                l += 1
                
            while l < r and slist[r] not in vowels:
                r -= 1
                
            tmp = slist[l]
            slist[l] = slist[r]
            slist[r] = tmp

            l += 1
            r -= 1
        
        return "".join(slist)

# Test the function
solution = Solution()
print(solution.reverseVowels("hello")
print(solution.reverseVowels("leetcode")
