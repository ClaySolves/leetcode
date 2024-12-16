class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        ans = []
        if n == 0: return []

        store = {}
        for num in nums:
            if num in store:
                store[num] += 1
            else:
                store[num] = 1

        maxStore = dict(sorted(store.items(), key= lambda x: -x[1]))
        print(maxStore)
        for i in range(k):
            ans.append(list(maxStore.keys())[i])

        return ans



def main():
    solution = Solution()
    print(solution.topKFrequent([3,0,1,0],1))

if __name__ == "__main__":
    main()