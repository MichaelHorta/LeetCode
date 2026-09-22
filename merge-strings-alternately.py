class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged=''
        max_len = len(word1)
        if len(word2) > max_len:
            max_len = len(word2)
        for i in range(max_len):
            if i < len(word1):
                merged=merged+word1[i]
            if i < len(word2):
                merged=merged+word2[i]
        return merged

def main():
    word1 = "ab"
    word2 = "pqrs"
    solution = Solution()
    result = solution.mergeAlternately(word1, word2)
    print(result)

if __name__ == "__main__":
    main()