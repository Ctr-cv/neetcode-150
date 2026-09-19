class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newstart, newend = newInterval[0], newInterval[1]
        i, idx = 0, 0
        inserted = False
        while i < len(intervals):
            start, end = intervals[i][0], intervals[i][1]
            if end < newstart:  # No overlap yet, continue
                i += 1
                continue
            elif start > newend:  # No more overlap at the end, return. Also handle no overlap case.
                if not inserted: intervals.insert(i, [newstart, newend])
                return intervals
            else:                   # Overlap appears
                if start <= newstart and end >= newend: # perfectly falls into an interval, no insertion
                    inserted = True
                    i += 1
                else:           # Some arbitrary overlap. We take the largest interval and continue.
                    newstart = min(newstart, start)
                    newend = max(end, newend)
                    intervals.pop(i)

        if not inserted: intervals.append([newstart, newend])
        return intervals

