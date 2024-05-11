class Solution:
    def isDigitSumPalindrome(self, n):
        #code here
         """
        Checks if the sum of digits of a number is a palindrome.

        """

        # Calculate the digit sum
        n = str(n) # Convert the number to a string
        digit_sum = sum(map(int,n))
        # Reverse the digit sum (using string conversion)
        reverse_sum = int(str(digit_sum)[::-1])

        # Check if the digit sum is a palindrome
        return 1 if digit_sum == reverse_sum else 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.isDigitSumPalindrome(N))
# } Driver Code Ends