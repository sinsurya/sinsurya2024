class Solution:
    def simpleInterest(self,A,B,C):
        #code here
        """
        Calculates the simple interest based on principal, rate, and time.

        """

        # Simple Interest formula: SI = (P * R * T) / 100
        return A*B*C/100

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        P,R,T=map(int,input().strip().split(' '))
        ob=Solution()
        print('%.2f'%ob.simpleInterest(P,R,T))
# } Driver Code Ends