class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        indexed = list(enumerate(position))
        indexed.sort(key = lambda x:x[1])
        st = []
        for t in indexed:
            time = (target - t[1]) / speed[t[0]]  # time taken w/o interruption
            st.append((t[0], time))
        fleets = 0
        fleet_time = 0
        while len(st) != 0:
            top = st.pop()
            if top[1] > fleet_time:
                fleet_time = top[1]
                fleets += 1
        return fleets
            
