class Solution:
    def modOfStrings(self, str1: str, str2: str) -> str:
            s1=str1
            while(len(s1) >= len(str2)):
                if s1.startswith(str2):
                    s1=s1[len(str2):]
                else:
                    break
            if s1 == str1:
                return 'none'
            return s1

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s1=str1
        s2=str2
        if len(str2) > len(str1):
            s1=str2
            s2=str1

        mod = self.modOfStrings(s1, s2)
        if mod == 'none':
            return ''
        if mod == '':
            return s2
        else:
            return self.gcdOfStrings(s2, mod)

def main():
    str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
    str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
    solution = Solution()
    result = solution.gcdOfStrings(str1, str2)
    print(result)

if __name__ == "__main__":
    main()