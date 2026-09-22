class Solution:
    def romanToInt(self, s: str) -> int:
        leng = len(s)
        sum=0
        i=1
        v=5
        x=10
        l=50
        c=100
        d=500
        m=1000
        ignore=False
        for j in range(leng):
            if ignore:
                ignore=False
                continue
            if s[j] == 'I' and j+1<leng and s[j+1] == 'V':
                sum=sum+4
                ignore=True
                continue
            if s[j] == 'I' and j+1<leng and s[j+1] == 'X':
                sum=sum+9
                ignore=True
                continue
            if s[j] == 'I':
                sum=sum+i
                continue
            if s[j] == 'V':
                sum=sum+v
                continue
            if s[j] == 'X' and j+1<leng and s[j+1] == 'L':
                sum=sum+40
                ignore=True
                continue
            if s[j] == 'X' and j+1<leng and s[j+1] == 'C':
                sum=sum+90
                ignore=True
                continue
            if s[j] == 'X':
                sum=sum+x
                continue
            if s[j] == 'L':
                sum=sum+l
                continue;
            if s[j] == 'C' and j+1<leng and s[j+1] == 'D':
                sum=sum+400
                ignore=True
                continue
            if s[j] == 'C' and j+1<leng and s[j+1] == 'M':
                sum=sum+900
                ignore=True
                continue
            if s[j] == 'C':
                sum=sum+c
                continue
            if s[j] == 'D':
                sum=sum+d
                continue
            if s[j] == 'M':
                sum=sum+m
                continue

        return sum

def main():
    sol = Solution()
    s="MCMXCIV"
    result = sol.romanToInt(s)
    print(result)

    
if __name__ == "__main__":
    main()