class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map={}
        i=0
        for num in nums:
            map[num]=i
            i=i+1

        j=0
        k=0
        for num in nums:
            diff=target-num
            if diff in map:
                k=map[diff]
                if k!=j:
                    break
            j=j+1

        return [j,k]

def main():
    nums = [1,3,3]
    target = 6
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)

if __name__ == "__main__":
    main()