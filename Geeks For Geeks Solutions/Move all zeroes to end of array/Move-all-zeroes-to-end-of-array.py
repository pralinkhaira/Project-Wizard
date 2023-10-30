class Solution:
    def pushZerosToEnd(self,arr, n):
        last_pos_idx = -1
        for i in range(n):
            if arr[i] > 0:
                arr[last_pos_idx + 1] = arr[i]
                if last_pos_idx + 1 < i: arr[i] = 0
                last_pos_idx += 1
        return arr
