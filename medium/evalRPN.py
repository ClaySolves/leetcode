class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        nums = []
        n = len(tokens)

        for i in range(n):
            if tokens[i] == '+':
                b = nums.pop()
                a = nums.pop()
                nums.append(a + b)

            elif tokens[i] == '-':
                b = nums.pop()
                a = nums.pop()
                nums.append(a - b)

            elif tokens[i] == '*':
                b = nums.pop()
                a = nums.pop()
                nums.append(a * b)

            elif tokens[i] == '/':
                b = nums.pop()
                a = nums.pop()
                nums.append(int(a / b))

            else:
                nums.append(int(tokens[i]))

        return nums[0]

def main():
    solution = Solution()
    print(solution.evalRPN(
        ["4","13","5","/","+"]
        ))

if __name__ == "__main__":
    main()