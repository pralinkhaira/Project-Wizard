class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def isRotated(self,str1,str2):
        #code here
        n = len(str1)

        # Check if str2 is obtained by rotating str1 to the left by 2 places
        rotated_left = str1[2:] + str1[:2]
        if str2 in rotated_left:
            return True

        # Check if str2 is obtained by rotating str1 to the right by 2 places
        rotated_right = str1[-2:] + str1[:-2]
        if str2 in rotated_right:
            return True

        # If no rotation is found
        return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        if(Solution().isRotated(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends