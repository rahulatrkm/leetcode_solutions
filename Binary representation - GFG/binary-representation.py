#User function Template for python3
class Solution:
	def getBinaryRep(self, n):
		# code here
		b = bin(n)[2:]
		return "0"*(30-len(b)) + b


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.getBinaryRep(n)
		print(ans)

# } Driver Code Ends