class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        sortNums = sorted(nums)
        print(sortNums)
        consecRun, ans = 0, 0
        for i in range(n-1):
            if sortNums[i] + 1 == sortNums[i+1]:
                consecRun += 1
            elif sortNums[i] == sortNums[i+1]:
                continue
            else:
                if consecRun:
                    if ans <= consecRun:
                        ans = consecRun + 1
                    consecRun = 0

        return max(consecRun+1, ans)
            

def main():
    solution = Solution()
    print(solution.longestConsecutive(
        [-9, -9, -9, -8, -5, -3, -3, -2, -1, 1, 8]
        ))

if __name__ == "__main__":
    main()   