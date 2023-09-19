class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        
        ans = []

        start = intervals[0][0]
        end = intervals[0][1]
        idx = 1
        while (idx < len(intervals)):
            opt = intervals[idx]
            opt_start = intervals[idx][0]
            opt_end = intervals[idx][1]
    
            if opt_start <= end:
                end = max(opt_end, end)
            else:
                ans.append([start, end])
                start = opt_start
                end = opt_end
            idx += 1

        ans.append([start, end])

        return ans