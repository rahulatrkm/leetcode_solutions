#User function Template for python3

class Solution:
    def findPosition(self, N):
        # code here 
        if (N == 0):
            return -1
        import math
        pos = math.log(N, 2)
        if pos%1 == 0:
            return int(pos+1)
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        
        ob = Solution()
        print(ob.findPosition(N))
# } Driver Code Ends