class MinStack:

    def __init__(self):
        self.MinStack = []

    def push(self, val: int) -> None:
         self.MinStack.append(val)

    def pop(self) -> None:
        self.MinStack.pop()

    def top(self) -> int:
        if self.MinStack:
            return self.MinStack[-1]
        else:
            return None

    def getMin(self) -> int:
        min = None
        myCopy = self.MinStack.copy()
        if myCopy:
            min = myCopy.pop()

        for i in range(len(myCopy)):
            val = myCopy.pop()
            if val < min: 
                min = val
        
        return min

                    
def main():
    solution = MinStack()
    solution = MinStack()
    solution.push(4)
    solution.push(3)
    solution.push(14)
    solution.push(2)
    solution.push(3)
    solution.push(0)
    solution.pop()
    param_3 = solution.top()
    param_4 = solution.getMin()
    print(param_3,param_4)

if __name__ == "__main__":
    main()   