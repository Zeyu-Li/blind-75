class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         resIntervals = []
#         todoStack = reversed(intervals)
#         inRange = False
#         while len(todoStack):
#             curr = todoStack.pop()
#             if newInterval[0] <= curr[0] < curr[1] <= newInterval[1]: continue
                
#             if newInterval[1] >= curr[0] and curr[1] <= newInterval[0]:
#                 newInterval[0] = curr[0]
#             elif newInterval[1] <= curr[0] and curr[1] >= newInterval[0]:
#                 newInterval[1] = curr[1]
                
#             if 
            
            
#         return resIntervals

        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: 
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)
        
        return res