class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if stack:
                if char == '}':
                    if '{' == stack[-1]:
                        stack.pop()
                    else:
                        return False

                elif char == ']':
                    if '[' == stack[-1]:
                        stack.pop()
                    else:
                        return False

                elif char == ')':
                    if '(' == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(char)
            else:
                stack.append(char)

        if len(stack) == 0: return True
        else: return False


def main():
    solution = Solution()
    print(solution.isValid(
        "]"
        ))

if __name__ == "__main__":
    main()   