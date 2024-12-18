class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)

        l = 0
        r = n-1
        ans = 0
        while(l < r):

            fillLimit = min(height[l],height[r])
            area = fillLimit * (r-l)

            if area > ans: ans = area

            if fillLimit == height[l]:
                store = height[l]
                while(l < r):
                    l+=1
                    if store < height[l]:
                        break
            else:
                store = height[r]
                while(l < r):
                    r-=1
                    if store < height[r]:
                        break

        return ans

def main():
    solution = Solution()
    print(solution.maxArea(
        []
        ))

if __name__ == "__main__":
    main()