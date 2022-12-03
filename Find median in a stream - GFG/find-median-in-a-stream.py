#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
import heapq
from collections import  defaultdict
import math


# } Driver Code Ends
#User function Template for python3

''' 
use globals min_heap and max_heap, as per declared in driver code
use heapify modules , already imported by driver code
'''
import heapq

class Solution:
    maxH = []
    minH = []
    def balanceHeaps(self):
        #Balance the two heaps size , such that difference is not more than one.
        # code here
        maxH = self.maxH
        minH = self.minH
        if (len(maxH)-len(minH)) > 1:
            curr = heapq.heappop(maxH)
            heapq.heappush(minH, -curr)
        if minH and maxH and minH[0] < -maxH[0]:
            c1 = heapq.heappop(minH)
            c2 = heapq.heappop(maxH)
            heapq.heappush(minH, -c2)
            heapq.heappush(maxH, -c1)
        
        
    '''    
    You don't need to call getMedian it will be called itself by driver code
    for more info see drivers code below.
    '''
    def getMedian(self):
        # return the median of the data received till now.
        # code here
        maxH = self.maxH
        minH = self.minH
        if len(maxH) > len(minH):
            return -maxH[0]
        return (minH[0]-maxH[0])//2
        
        
    def insertHeaps(self,x):
        #:param x: value to be inserted
        #:return: None
        # code here
        maxH = self.maxH
        minH = self.minH
        heapq.heappush(maxH, -x)
        self.balanceHeaps()
        # print(x, maxH, minH)
        

#{ 
 # Driver Code Starts.

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        ob=Solution()
        for i in range(n):
            x=int(input())
            ob.insertHeaps(x)
            print(math.floor(ob.getMedian()))

# } Driver Code Ends