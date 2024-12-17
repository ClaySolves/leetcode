class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        myParen = []
        paren = []

        def build(open,closed):

            if open == closed == n:
                myParen.append(''.join(paren))
                return

            if open < n:
                paren.append('(')
                build(open+1,closed)
                paren.pop()

            if closed < open:
                paren.append(')')
                build(open,closed+1)
                paren.pop()

        build(0,0)

        return myParen


def main():
    solution = Solution()
    print(solution.generateParenthesis(
        13
        ))

if __name__ == "__main__":
    main()