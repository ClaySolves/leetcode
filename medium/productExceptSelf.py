class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [1] *  n
        pre = [1] *  n
        post = [1] *  n

        preProd = nums[0]
        postProd = nums[n-1]
        for i in range(n):
            if i == 0:
                post[n-1] = nums[n-1]
                pre[0] = nums[0]
                continue
            preProd *= nums[i]
            postProd *= nums[n-i-1]
            pre[i] = preProd
            post[n-i-1] = postProd

        for i in range(n):
            if i == 0:
                ans[i] = post[1]
            elif i == n-1:
                ans[i] = pre[n-2]
            else:
                ans[i] = pre[i-1] * post[i+1]

        return ans
                    
def main():
    solution = Solution()
    print(solution.productExceptSelf([1,2,3,4]))

if __name__ == "__main__":
    main()   