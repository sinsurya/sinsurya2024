class Solution:
    def get(self, a, b):
        """
        Swaps two numbers (a and b) and returns them in a list in the reversed order (b, a).

        """
        return [b, a] 

#{ 
 # Driver Code Starts.
if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		a,b = map(int,input().strip().split())
		ob = Solution()
		ans=ob.get(a,b)
		print(str(ans[0])+" "+str(ans[1]))
# } Driver Code Ends