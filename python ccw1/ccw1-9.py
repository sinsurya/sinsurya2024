class Solution:
    def oddEven (ob,N):
        # code here 
        """
        Checks if a number is odd or even and returns a string indicating the result.
        """
        # Use modulo operator (%) to check for divisibility by 2
        return "odd" if N%2==1 else "even" 

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N=int(input())

        ob = Solution()
        print(ob.oddEven(N))
# } Driver Code Ends