
class Solution:
    def reverse_digit(self, n: int) -> int:
        """
        Reverses the digits of an integer
        """
        return int(str(n)[::-1])  
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.reverse_digit(n)
		print(ans)
# } Driver Code Ends                                    