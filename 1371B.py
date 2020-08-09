t = int(input())

for testcase in range(t):
    n,r = map(int,input().split())

    if n>r:
        ans= (r*(r+1))//2
    else:
        ans = (n*(n+1))//2
        ans -=(n-1)

    print(ans)