class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        if len(strs) < 1: return [[]]

        store = {}
        ans = []
        for str in strs:
            newStr = ''.join(sorted(str))
            if newStr in store:
                ans[store[newStr]].append(str)
            else:
                store[newStr] = len(ans)
                ans.append([str])

        return ans


def main():
    solution = Solution()
    print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

if __name__ == "__main__":
    main()