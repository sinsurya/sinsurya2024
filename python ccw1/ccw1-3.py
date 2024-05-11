class Solution:
    def armstrong (self, n):
        """
        Checks if a given number is an Armstrong number (sum of digit cubes equals the number itself).

        """
        # Convert the integer to a string to access digits
        num_str = str(n)

        # Handle numbers with less than 3 digits (not Armstrong numbers)
        if len(num_str) < 3:
            return "No"

        # Calculate the sum of cubes of digits
        sum_cubes = 0
        for digit in num_str:
            sum_cubes += int(digit) ** 3

        # Check if the sum equals the original number
        return "Yes" if sum_cubes == n else "No"

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrong(n))
# } Driver Code Ends