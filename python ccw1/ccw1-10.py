class Solution:
    def getTable(self,N):
        # code here
        """
        Generates the multiplication table of a given number (N) and returns it as a list.

        """

        # Use list comprehension for concise table generation
        return  [N*i for i in range(1,11)] 
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.getTable(N)
        for i in ans:
            print(i,end=" ")
        print()
# } Driver Code Ends