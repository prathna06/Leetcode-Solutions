class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sortedCitations = sorted(citations, reverse=True)
        hIndex = 0
        for i in range(len(sortedCitations)):
            if sortedCitations[i] <= i+1 and sortedCitations[i] > hIndex:
                hIndex = sortedCitations[i]
            elif sortedCitations[i] > i+1 and sortedCitations[i] > hIndex:
                hIndex = i+1

        return hIndex

#         totalPaper = len(citations)
#         hIndex = 0
#         sortedArr = sorted(citations)
#         array = [x for x in sortedArr if x > 0]
#         if len(array) == 1 and array[0] > 0 :
#             return 1
        
#         for i in range(len(sortedArr)):
#             if len(sortedArr) - i >= sortedArr[i]:
#                 hIndex = sortedArr[i]
#             print(hIndex)
#         return hIndex
# # 01356
# # 5
