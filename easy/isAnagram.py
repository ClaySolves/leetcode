class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        newS = ''.join(sorted(s))
        newT = ''.join(sorted(t))

        return newT == newS
    
def main():
    solution = Solution()
    print(solution.isAnagram("ab","a"))

if __name__ == "__main__":
    main()