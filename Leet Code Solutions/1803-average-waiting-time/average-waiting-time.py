class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        prepare, n=0, len(customers)
        return sum((prepare:=max(t[0],prepare)+t[1])-t[0] for t in customers)/n