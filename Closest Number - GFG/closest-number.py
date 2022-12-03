#User function Template for python3

class Solution:
    def closestNumber(self, N , M):
        # code here 
        if N%M == 0:
            return N
        if M > 0:
            rem = N%M
            rem1 = M-rem
            # print(rem, rem1)
            if rem < rem1:
                return N-rem
            elif rem > rem1:
                return N+rem1
            else:
                if abs(N+rem) > abs(N-rem):
                    return N+rem
                else:
                    return N-rem
        
        else:
            rem = N%M
            rem1 = M-rem
            # print(rem, rem1)
            if rem < rem1:
                return N+rem1
            elif rem > rem1:
                return N-rem
            else:
                if abs(N+rem) > abs(N-rem):
                    return N+rem
                else:
                    return N-rem

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,M=map(int,input().split())
        
        ob = Solution()
        print(ob.closestNumber(N,M))
# } Driver Code Ends