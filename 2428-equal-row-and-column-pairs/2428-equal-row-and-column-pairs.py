from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = defaultdict(int) #defaultdict assigns value to 0 for each key
        pair = 0 
        for row in grid:
            rows[tuple(row)] += 1 # we need to convert list to tuple as list are mutable and keys of a dict can't be mutable

        for col in range(len(grid)):
            column = tuple(grid[r][col] for r in range(len(grid))) # we need to use list Compression to get the value of columns 
            if column in rows:
                pair += rows[column]
        return pair



  

