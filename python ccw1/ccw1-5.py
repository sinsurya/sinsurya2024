class Solution:
    def gcd(self, a: int, b: int) -> int:
        """
        Calculates the GCD of two positive integers using the Euclidean Algorithm.

        """
        # Implement the Euclidean Algorithm for GCD calculation
        while b != 0:
            remain = a % b
            a = b
            b = remain
        return a  # GCD is the value of a when b becomes 0
 
#{ 
 # Driver Code Starts

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a = int(input())
        
        
        b = int(input())
        
        obj = Solution()
        res = obj.gcd(a, b)
        
        print(res)

# } Driver Code Ends