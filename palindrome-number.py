class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        x_str = str(x)
        leng = len(x_str)
        half_len = int(leng/2)
        for i in range(half_len):
            if x_str[i] != x_str[leng-i-1]:
                return False

        return True

def main():
    sol = Solution()
    x=-0
    #print(len(str(x))/2)
    result = sol.isPalindrome(x)
    print(result)
    
if __name__ == "__main__":
    main()