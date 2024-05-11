class Solution:
    def findNthTerm(self, N):
        # code here 
        """
        Calculates the Nth term in the series where each term is the sum of the previous term and its position.

        """
        
        # The series represents the sum of natural numbers from 1 to N
        # Use the formula n * (n + 1) / 2 to calculate the sum efficiently
        return N * (N + 1) // 2


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.findNthTerm(N))
# } Driver Code Ends