#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        i,j,k = 0,0,n-1
        while i <= k:
            if arr[i] == 0:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j += 1
            elif arr[i] == 2:
                arr[i], arr[k] = arr[k], arr[i]
                k -= 1
            else:
                i += 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends