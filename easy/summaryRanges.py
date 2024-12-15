class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        addArrow = "->"
        n = len(nums)
        ans = []
        continueRange = False
        rangeStart = nums[0]

        for i in range(n-1):
            if nums[i+1] == nums[i] + 1:
                if not continueRange:
                    continueRange = True
                    rangeStart = nums[i]
            else:
                if continueRange:
                    ans.append(f"{rangeStart}{addArrow}{nums[i]}")
                else:
                    ans.append(str(nums[i]))
                continueRange = False
        
        if continueRange:
            ans.append(f"{rangeStart}{addArrow}{nums[-1]}")
        else:
            ans.append(str(nums[-1]))
            
        return ans

def main():
    solution = Solution()
    print(solution.summaryRanges([0,1,2,4,5,7]))

if __name__ == "__main__":
    main()