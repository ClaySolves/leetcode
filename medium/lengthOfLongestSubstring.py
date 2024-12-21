class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        ans = 0
        for i in range(n):
            store = set()
            store.add(s[i])
            for k in range(i+1,n):
                if s[k] in store:
                    ans = max(ans,len(store))
                    break
                else:
                    store.add(s[k])
            ans = max(ans,len(store))

        return ans
            

def main():
    solution = Solution()
    print(solution.lengthOfLongestSubstring(
        "hfiesonfiesndwadwadnm"
        ))

if __name__ == "__main__":
    main()