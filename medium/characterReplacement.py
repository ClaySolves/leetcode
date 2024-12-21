class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        store = {}
        ans = 0
        l = 0
        n = len(s)
        maxVal = 0

        for r in range(n):
            store[s[r]] = 1 + store.get(s[r],0)

            maxVal = max(store[s[r]],maxVal)

            while((r - l + 1) - maxVal > k):
                store[s[l]] -= 1
                l += 1

            ans = max(r-l+1,ans)

        return ans
    
    
def main():
    solution = Solution()
    print(solution.characterReplacement(
        "JDIKWAJDOWPSKODKLOPKOPDKLDOPLDODDPLDPOWLADOPWA", 7
        ))

if __name__ == "__main__":
    main()