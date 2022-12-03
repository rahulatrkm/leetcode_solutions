#User function template for Python 3

class Solution:
    def convertRoman(self, n):
        #Code here
        ans = []
        while n:
            if n>=1000:
                ans.append('M'*(n//1000))
                n %= 1000
            elif n>=900:
                ans.append('CM')
                n %= 900
            elif n>=500:
                ans.append('D'*(n//500))
                n %= 500
            elif n>=400:
                ans.append('CD')
                n %= 400
            elif n>=100:
                ans.append('C'*(n//100))
                n %= 100
            elif n>=90:
                ans.append('XC')
                n %= 90
            elif n>=50:
                ans.append('L'*(n//50))
                n %= 50
            elif n>=40:
                ans.append('XL')
                n %= 40
            elif n>=10:
                ans.append('X'*(n//10))
                n %= 10
            elif n>=9:
                ans.append('IX')
                n %= 9
            elif n>=5:
                ans.append('V'*(n//5))
                n %= 5
            elif n>=4:
                ans.append('IV')
                n %= 4
            elif n>=1:
                ans.append('I'*n)
                n %= 1
        return "".join(ans)

#{ 
 # Driver Code Starts
#Initial template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        ob = Solution()
        print(ob.convertRoman(n))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends