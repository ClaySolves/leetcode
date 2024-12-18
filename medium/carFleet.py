class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        n = len(position)
        myAns = []
        sortedLists = sorted(zip(position,speed))
        newPos, newSpeed = zip(*sortedLists)

        for i in range(n):
            trips =(target-newPos[i])/newSpeed[i]
            if myAns:
                while trips >= myAns[-1]:
                    myAns.pop()
                    if not myAns: break

            myAns.append(trips)

        return int(len(myAns))
            
def main():
    solution = Solution()
    print(solution.carFleet(
        target = 31, position = [5,26,18,25,29,21,22,12,19,6], speed = [7,6,6,4,3,4,9,7,6,4]
        ))

if __name__ == "__main__":
    main()