# https://leetcode.com/problems/design-a-number-container-system/description/?envType=daily-question&envId=2025-02-08
from collections import defaultdict
import heapq

class NumberContainers:

    def __init__(self):
        self.idxToNumber = defaultdict(int)
        self.numToIndex = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.idxToNumber[index] = number
        heapq.heappush(self.numToIndex[number], index)
        
    def find(self, number: int) -> int:
        currentHeap = self.numToIndex[number]
        if len(currentHeap) == 0: 
            return - 1
        while self.idxToNumber[currentHeap[0]] != number:
            heapq.heappop(currentHeap)
            if len(currentHeap) == 0:
                return -1
        return currentHeap[0]

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)