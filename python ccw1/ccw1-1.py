class Solution:
    def seriesSum(self, n : int) -> int:
        # code here
        sum=(n*(n+1)//2)
        return sum

#{
# driver code starts
if __name__=='__main__':
    t= int(input())
    for _ in range(t):
        n=int(input())
        obj=Solution()
        res=obj.seriesSum(n)
        print(res)
# }driver code ends