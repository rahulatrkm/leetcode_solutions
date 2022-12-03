#User function Template for python3

class Solution:
    def replaceBit(self, N, K):
        # code here
        li = list(bin(N))
        if K > len(li)-2:
            return N
        li[k+1] = "0"
        # print(li)
        return int("".join(li), 2)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n,k = input().strip().split(" ")
        n,k = int(n), int(k)
        ob = Solution()
        ans = ob.replaceBit(n,k)
        print(ans)
# } Driver Code Ends