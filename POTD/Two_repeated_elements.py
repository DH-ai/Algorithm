class Solution:
    
    #Function to find two repeated elements.
    def twoRepeated(self, arr , n):
        #Your code here
        max1 = max(arr)
        ans=[0]*2
        #requency so that ik which no. is appearing twice in O(n)
        freq = [0]*(max1+1)
        
        for i in range(n+2):
            freq[arr[i]]+=1
            
        # print(freq)
        # checking the num which are appearing twice
        temp=[]
        for i in range(max1+1):
            if freq[i]==2:
                temp.append(i)
                
        #checking for the indes which one is bigger for 
        index1 = self.secondAppearenceIndex(arr,temp[0],n+2)
        index2 = self.secondAppearenceIndex(arr,temp[1],n+2)
        if index1>index2:
            ans[0]=temp[1]
            ans[1]=temp[0]
        else:
            ans[0]=temp[0]
            ans[1]=temp[1]
        
        return ans
        
        
    def secondAppearenceIndex(self,arr,num,n):
        cnt=0
        for i in range(n):
            if arr[i]==num:
                # print(f"num:{num},{i}")
                cnt+=1
                if cnt==2:
                    
                    return i

# 4 size of array is n+2
# 1 2 1 3 4 3  custom input to check 

################ METHOD 2
class Solution:
  
    
    #Function to find two repeated elements.
    def twoRepeated(self, arr , n):
        res = []
        first = False

        for i in range(n+2):# iterating over each element of array 
            #making the visited elements negative
            if arr[abs(arr[i])]>0:
                arr[abs(arr[i])]*=-1
            #if the number is negative, it was visited previously
            #so this would be the repeated element.
            else:
                #storing first and second repeated element accordingly.
                #this first = false result help when the element which was founf negative first does not matter its value it will be first in the result array
                if first ==False:
                    res.append(abs(arr[i]))
                    first = True
                else:
                    res.append(abs(arr[i]))
        return res