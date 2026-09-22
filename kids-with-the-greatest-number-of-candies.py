class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        greaterAmountOfCandies = max(candies)
        list = []
        for candy in candies:
            if candy + extraCandies >= greaterAmountOfCandies:
                list.append(True)
            else:
                list.append(False)

        return list

def main():
    sol = Solution()
    candies = [4,2,1,1,2]
    extraCandies = 1
    result = sol.kidsWithCandies(candies, extraCandies)
    print(result)

if __name__ == "__main__":
    main()