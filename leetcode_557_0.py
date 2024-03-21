class Solution:
    def reverseWords(self, s: str) -> str:
        slist = s.split(' ')
        rev = []
        for i in slist:
            w = i[::-1]
            rev.append(w)
        return " ".join(rev)
