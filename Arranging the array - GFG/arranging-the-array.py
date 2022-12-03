#User function Template for python3

def Rearrange( a, n):
    # Your code goes here
    a1, a2 = [], []
    for num in a:
        if num < 0:
            a1.append(num)
        else:
            a2.append(num)
    a[:len(a1)] = a1
    a[len(a1):] = a2




#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        Rearrange(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends