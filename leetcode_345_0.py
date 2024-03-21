class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        slist = list(s)
        i, j = 0, len(slist) - 1

        while (i < j):
            if slist[i] not in vowels:
                i += 1
                continue
            if slist[j] not in vowels:
                j -= 1
                continue
            slist[i], slist[j] = slist[j], slist[i]
            i += 1
            j -= 1

        return "".join(slist)

# Test the function
solution = Solution()
print(solution.reverseVowels("hello")
print(solution.reverseVowels("leetcode")

# Time: O(n) - Linear - where n is the length of the input string s. The two pointers i and j move towards each other, and each character is processed once.
# Space: O(n) - Linear - because we create a list to store the characters of the input string. The space used is proportional to the length of the input string. Other than that, we use a constant amount of extra space for the vowels string and a few integer variables, which doesn't depend on the input size.
