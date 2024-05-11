class Solution:
	def find_median(self, v):
		# Code here
		v.sort()
		l=len(v)
		m=l//2
		if l%2==0:
		    return (v[m-1]+v[m])//2
		else:
		    return v[m]
		
#{
#driver code starts
#initial template for python3

if __name__=='__main__':
	T=int(input())
	for i in range(T):
		n=int(input())
		v=list(map(int,input().split()))
		ob=Solution()
		ans=ob.find_median(v)
		print(ans)
#}driver code ends