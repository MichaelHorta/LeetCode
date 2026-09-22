class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        r = 0
        first=strs[0]
        prefix=''
        i=0
        for c in first:
            prefix=prefix+c
            for s in strs:
                if i == 0:
                    i=i+1
                    continue
                if s.startswith(prefix) == False:
                    return prefix[:-1]
            r=r+1

        return prefix

def main():
    strs = ["flod","flowc","flowx"]
    #strs = ["dog","racecar","car"]
    solution = Solution()
    result = solution.longestCommonPrefix(strs)
    print(result)

if __name__ == "__main__":
    main()