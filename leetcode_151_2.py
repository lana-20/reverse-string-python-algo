class Solution:
    def reverseOneWord(self, s: list, debut: int, fin: int):
        i = debut
        j = fin
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    def deleteSpacesSeries(self, s: list):
        i = len(s)-1
        while i >= 0 and s[i].isspace():
            s.pop()
            i -= 1

        i = 0
        while i < len(s) and s[i].isspace():
            i += 1

        write_i = 0
        while i < len(s):
            if not (s[i - 1].isspace() and s[i].isspace()):
                s[write_i] = s[i]
                write_i += 1
            i += 1

        for _ in range(len(s) - write_i):
            s.pop()

    def reverseWords(self, s: str) -> str:
        s = list(s)

        self.reverseOneWord(s, 0, len(s) - 1)

        i = 0
        motDebut = 0
        motFin = 0
        estMotFini = False

        while i < len(s):
            if s[i].isspace():
                if estMotFini:
                    self.reverseOneWord(s, motDebut, motFin)
                    estMotFini = False
            elif not estMotFini:
                    estMotFini = True
                    motDebut = i
                    motFin = i
            else:
                motFin += 1
            i+=1

        if estMotFini:
            self.reverseOneWord(s, motDebut, motFin)

        self.deleteSpacesSeries(s)

        return "".join(s)
