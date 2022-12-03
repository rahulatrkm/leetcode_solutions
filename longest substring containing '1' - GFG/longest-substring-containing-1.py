#User function Template for python3

def maxlength(s):
    
    #add code here
    m = 0
    curr = 0
    for char in s:
        if char == "1":
            curr += 1
        else:
            curr = 0
        m = max(m, curr)
    m = max(m, curr)
    return m


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        s=input()
        print(maxlength(s))
# } Driver Code Ends