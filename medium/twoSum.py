class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []


    def twoSumSlow(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        for i in range(n):
            need = target - numbers[i]
            newList = numbers.copy()
            newList.remove(numbers[i])
            if need in newList:
                if need == numbers[i]:
                    index = numbers.index(need)
                    realIndex = numbers.index(need,index+1)
                    return (i+1,realIndex+1)         
                return (i+1,numbers.index(need)+1)                
        return None

def main():
    solution = Solution()
    print(solution.twoSum(
        [0,0,3,4],0
        ))

if __name__ == "__main__":
    main()