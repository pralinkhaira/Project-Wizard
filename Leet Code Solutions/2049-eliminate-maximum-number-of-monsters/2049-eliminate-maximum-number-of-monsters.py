class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time_to_city = [dist[i] / speed[i] for i in range(len(dist))]
        time_to_city.sort()
        
        for i in range(len(time_to_city)):

            if time_to_city[i] <= i:
                return i

        return len(dist)