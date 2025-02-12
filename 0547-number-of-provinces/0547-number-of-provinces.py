from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        pipeline = deque()
        pipeline.append(0)
        totalNodes = len(isConnected)
        nonVisitedList = [n for n in range(totalNodes)]
        noOfProvince = 0    
        if sum(isConnected[0]) == totalNodes:
            return 1
        while len(nonVisitedList):       
            ele = pipeline.popleft()
            nonVisitedList.remove(ele)
            for i in range(totalNodes):
                if isConnected[ele][i] == 1 and i != ele and i in nonVisitedList and i not in pipeline :
                    pipeline.append(i)
            if len(pipeline) == 0:
                noOfProvince += 1
                if len(nonVisitedList) > 0:
                    pipeline.append(nonVisitedList[0])

        return noOfProvince            

                    

        