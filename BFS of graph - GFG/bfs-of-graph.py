#User function Template for python3

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        import collections
        q = collections.deque()
        ans = []
        q.append(0)
        vis = set()
        while q:
            curr = q.popleft()
            if curr in vis:
                continue
            vis.add(curr)
            ans.append(curr)
            for i in adj[curr]:
                if i in vis:
                    continue
                q.append(i)
        return ans
        

#{ 
 # Driver Code Starts

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends