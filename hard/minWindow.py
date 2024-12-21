class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        ans = n
        l = 0


        storeT = {}
        for i in range(len(t)):
           storeT[s[i]] = 1 + storeT.get(s[i],0)
        
        storeS = {}
        for r in range(n):
            storeS[s[r]] = 1 + storeS.get(s[r],0)

            if storeS >= storeT:
                ans = min(ans,len(storeS))

            if ans < len(storeS):
                storeS[s[l]] -= 1
                l += 1

            
def main():
    solution = Solution()
    print(solution.minWindow(
        "ADOBECODEBANC", "ABC"
        ))

if __name__ == "__main__":
    main()