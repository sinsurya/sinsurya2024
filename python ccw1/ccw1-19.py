class Solution:
    def count_divisors(self, N):
        # Count of divisors divisible by 3 (initialize to 0)
        cnt = 0

        # Iterate only up to the square root of N for efficiency
        for i in range(1, int(N**0.5) + 1):
            if N % i == 0:
                # If i is divisible by 3, add 2 (i and N/i are both divisors divisible by 3)
                if i % 3 == 0: cnt += 2 
                # Else, add 1 (only i is a divisor)
                else: cnt += 1

        return cnt
#{ 
 # Driver Code Starts
#Initial Template for Python 3#Back-end complete function Template for Python 3#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.count_divisors(N))
# } Driver Code Ends