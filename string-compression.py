class Solution:
    def compress(self, chars: list[str]) -> int:
        c=1
        j=0
        for i in range(len(chars)):
            if i + 1 < len(chars) and chars[i + 1] == chars[i]:
                c+=1
            else:
                if c == 1:
                    chars[j]=chars[i]
                    j+=1
                else:
                    chars[j] = chars[i]
                    j+=1
                    c_len = len((str)(c))
                    for k in range(c_len):
                        mod = c%pow(10,(c_len-k))
                        div = mod/pow(10,(c_len-k-1))
                        div_int = (int)(div)
                        chars[j] = (str)(div_int)
                        j+=1
                
                c=1
                
        chars=chars[:j]

        return len(chars)

def main():
    solution = Solution()
    #a2=2
    #a10=3
    #a18=3
    #print(solution.compress(["a","a","b"]))
    #print(solution.compress(["a","a","b","b","c","c","c"]))
    print(solution.compress(["a","a","a","a","a","a","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","c","c","c","c","c","c","c","c","c","c","c","c","c","c"]))
    #print(solution.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
    #print(solution.compress(["a", "a", "a", "b", "b", "a", "a"]))

if __name__ == "__main__":
    main()