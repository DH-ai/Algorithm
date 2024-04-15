#User function Template for python3
class Solution:
    def countElements(self, a, b, n, query, q):

        #maximum element of a: max
        max1=-1
        for elem in a:
            if elem > max1 : max1 = elem
        
        max2 = -1
        #maximum elem of b: max2
        for elem in a:
            if elem > max2 : max2 = elem
        
        #frequency array of b
        h = [0]*(max2+1) 
        for i in range (max2+1):
            h[b[i]]+=1

        #commulative frequency array of b

        for i in range (1,max+1):
            h[i] += h[i-1]

        ans = []

        # finding the answer 
        for i in q:
            ans.append(h[a[i]])
        
        return ans 
#{ 
 # Driver Code Starts
#Initial Template for Python 3
t = int(input())
for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = int(input())
    query = []
    ob = Solution()
    for i in range(q):
        query.append(int(input()))
    ans = ob.countElements(a, b, n, query, q)
    for i in range(q):
        print(ans[i])

# } Driver Code Ends

""" 
custom input 
4
1 1 5 5
0 1 2 3
4
0
1
2
3


"""

