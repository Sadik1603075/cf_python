t = int(input())

for testcase in range(t):
    a,b,n,m=map(int,input().split())

    if(a+b<n+m):
        print('NO\n')
        continue
    if(min(a,b)<m):
        print('NO\n')
        continue
    print('YES\n')