class Solution:
    def oppositeFaceOfDice(self, N):
        """
        Finds the opposite face on a standard 6-sided die given a face number (N).
            
        """
        # Calculate the opposite face using the property: sum of opposite faces is 7
    	#code here 
        return 7-N

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.oppositeFaceOfDice(N)
        print(ans)
# } Driver Code Ends