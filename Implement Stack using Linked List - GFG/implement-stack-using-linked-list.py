class StackNode:
    # Constructor to initialize a node
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class MyStack:

        
    #Function to push an integer into the stack.
    head = None
    def push(self, data):
        node = StackNode(data)
        tail = self.head
        while tail and tail.next:
            tail = tail.next
            
        if not tail:
            self.head = node
        else:
            tail.next = node


    #Function to remove an item from top of the stack.
    def pop(self):
        if not self.head:
            return -1
            
        curr = self.head
        while curr and curr.next and curr.next.next:
            curr = curr.next
        if curr and curr.next:
            val = curr.next.data
            curr.next = None
            return val
        elif curr:
            val = curr.data
            self.head = None
            return val
        return -1
    
    def isEmpty(self):
        return self.head == None
    

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = MyStack()
        q = int(input())
        q1 = list(map(int, input().split()))
        i = 0
        while(i < len(q1)):
            if(q1[i] == 1):
                s.push(q1[i + 1])
                i = i + 2
            elif(q1[i] == 2):
                print(s.pop(), end=" ")
                i = i + 1
            elif(s.isEmpty()):
                print(-1)
        print()

# } Driver Code Ends