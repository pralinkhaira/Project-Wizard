#User function Template for python3

class Solution:
    def findString(self, N, K):
        def __init__(self):
            self.a = None

        def dfs(n, k, string, ans):
            if n == 0:
                ans.add(string)
                return ans

            for i in range(k):
                ans = dfs(n - 1, k, string + str(i), ans)
            return ans

        def find(ele, string):
            vis.add(ele)
            if len(vis) == (K ** N):
                self.a = string
                return True

            for y in graph[ele]:
                if y not in vis and find(y, string + y[-1]):
                    return True
            vis.remove(ele)
            return False

        ans = set()
        ans = dfs(N, K, '', ans)
        graph = {}
        for i in ans:
            for z in range(K):
                ele = i[1:] + str(z)
                if ele in ans and ele != i:
                    if i in graph:
                        graph[i].append(ele)
                    else:
                        graph[i] = [ele]

        vis = set()
        for i in ans:
            if find(i, i):
                return self.a
        return self.a






#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())

        ob = Solution()
        ans = ob.findString(N,K)
        ok = 1
        for i in ans:
            if ord(i)<48 or ord(i)>K-1+48:
                ok = 0
        if not ok:
            print(-1)
            continue
        d = dict()
        i = 0
        while i+N-1<len(ans):
            d[ans[i:i+N]] = 1
            i += 1
        tot = pow(K,N)
        if len(d)==tot:
            print(len(ans))
        else:
            print(-1)
# } Driver Code Ends