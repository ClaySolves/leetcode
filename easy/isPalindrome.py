class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''.join(foundChar.lower() for foundChar in s if foundChar.isalnum())
       
        n = len(newStr)
        l = 0
        r = n-1
        for i in range(int(n/2)):
            if newStr[l+i] == newStr[r-i]:
                continue
            else:
                return False
        return True

    

def main():
    solution = Solution()
    print(solution.isPalindrome(
        "A man, a plan, a canaal: Panama"
        ))

if __name__ == "__main__":
    main()