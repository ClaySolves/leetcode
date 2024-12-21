class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        l = 0
        r = 1
        ans = 0

        while(l<n):
            if height[l] == 0:
                l+=1
                r=l+1
                continue

            store = height[l]
            while(store < height[r]):
                r+=1


def main():
    solution = Solution()
    print(solution.trap(
        [0,1,0,2,1,0,1,3,2,1,2,1]
        ))

if __name__ == "__main__":
    main()