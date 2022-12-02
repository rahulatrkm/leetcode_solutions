#User function Template for python3
class Solution:
	def minJumps(self, arr, n):
	    if n == 1:
	        return 0
        if arr[0] == 0:
            return -1
	    reach = arr[0]
	    steps = arr[0]
	    jumps = 1
	    for i in range(1, n-1):
	        reach = max(reach, i+arr[i])
	        steps -= 1
	        if steps == 0:
	            jumps += 1
	            if (i >= reach):
	                return -1
                steps = reach-i
        return jumps


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends