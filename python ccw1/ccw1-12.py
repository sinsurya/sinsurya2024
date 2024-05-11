class Solution:
    def nPr(self, n, r):
        """
        Calculates the number of permutations (nPr) using a formula.

        """

        # Input validation: check if r is within valid range (0 to n)
        if r > n or r < 0:
            raise ValueError("Invalid input: r cannot be greater than n or negative.")

        # Formula for nPr: n! / (n - r)! = n(n-1)(n-2)(n-3)......(n-r)
        # Here, we calculate it iteratively for efficiency
        i, pro = 0, 1
        for i in range(0, r): pro *= (n - i)
        return pro
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nPr(n, r))
# } Driver Code Ends