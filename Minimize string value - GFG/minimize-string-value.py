#User function Template for python3
import heapq

class Solution:
	def minValue(self, S, k):
		# code here
		d = {}
		for char in S:
		    d[char] = d.get(char, 0) + 1
	    vals = [num*-1 for num in d.values()]
	        
	    heapq.heapify(vals)
	   # print(vals)
	    while k and vals:
	        curr = heapq.heappop(vals)
	        if vals:
	            top = vals[0]
    	        diff = min(k, top-curr+1)
    	        if curr+diff < 0:
    	            heapq.heappush(vals, curr+diff)
    	        k -= diff
            else:
                if k+curr < 0:
                    heapq.heappush(vals, curr+k)
                    k = 0
        ans = sum(num**2 for num in vals)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s,k = input().split()
		k = int(k)

		ob = Solution()
		answer = ob.minValue(s,k)
		print(answer)

# } Driver Code Ends