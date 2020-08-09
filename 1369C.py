t = int(input())

for testcase in range(t):
    n,k = map(int,input().split())
    a=list(map(int,input().split()))
    w= list(map(int,input().split()))
    
    a.sort(reverse=True)
    w.sort()

    sum=0

    for i in range(k):
        if w[i]==1:
            sum += a[i]*2
        else:
            sum += a[i]
        w[i]-=1
    w.reverse()
    j = n-1
    indx=0
    for i in range(k):
        if w[i]==0:
            break
        sum += a[j]
        j -= w[i]
    
    print(sum)




    

