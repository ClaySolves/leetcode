class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        l = 0
        r = 1
        ans = 0

        while r < n:
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                ans = max(ans,prices[r] - prices[l])
                r += 1

        return ans
    
def main():
    solution = Solution()
    print(solution.maxProfit(
        [7,1,5,3,6,4]
    ))

if __name__ == "__main__":
    main()