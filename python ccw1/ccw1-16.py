class Solution:
    def greatestOfThree(self,A,B,C):
        #code here  
        """
        Finds the greatest of three numbers using the built-in `max` function.

        """

        # Use the built-in max function to find the largest number
        return max(A, B, C) 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        A,B,C=map(int,input().strip().split(' '))
        ob=Solution()
        print(ob.greatestOfThree(A,B,C))   
# } Driver Code Ends