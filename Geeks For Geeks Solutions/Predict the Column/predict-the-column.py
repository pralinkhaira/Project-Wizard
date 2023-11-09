class Solution:
    def columnWithMaxZeros(self,arr,N):
        ans=-1
        res=N
        for i in range(N):
            temp=0
            for j in range(N):
                temp+=arr[j][i]
            if temp<res:
                res=temp
                ans=i
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = []
        for i in range(N):
            line = [int(x) for x in input().strip().split()]
            arr.append(line)
        ob=Solution()
        print(ob.columnWithMaxZeros(arr,N))


# } Driver Code Ends