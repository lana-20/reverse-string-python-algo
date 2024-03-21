class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        reverse = True
        result = ""
        for i in range(0, len(s), k):
            sub = s[i : i + k]
            if reverse:
                result += sub[::-1]
            else:
                result += sub
            reverse = not reverse
        return result
