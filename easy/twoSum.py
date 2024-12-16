class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)

        for i in range(n-1):
            for k in range(i+1,n):
                if nums[i] + nums[k] == target:
                    return [i,k]
  

def main():
    solution = Solution()
    print(solution.twoSum([3,2,4],6))

if __name__ == "__main__":
    main()