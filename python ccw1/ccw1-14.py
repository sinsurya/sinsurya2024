class Solution:
	def streamAvg(self, arr, n):
		# code here
        """
        Calculates the average of a stream of numbers at every point in the stream.

        """

        # Initialize an empty list to store averages
        averages = []

        # Calculate the sum and average for each element in the stream
        sum_so_far = 0
        for num in arr:
            sum_so_far += num
            average = sum_so_far / (len(averages) + 1)  # Include current element in average
            averages.append(average)

        return averages


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.streamAvg(arr, n)
        for x in ans:
            print('%.2f'%x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends