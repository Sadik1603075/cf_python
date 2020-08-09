import collections
t = int(input())

for tesecase in range(t):
    n,k = map(int,input().split())
    s = input()
    str = "1"+s+"1"
    alist = []

    sum=0
    
    for i in range(1,n+1):
        if str[i]=='1':
            alist.append(i)
            alist.append(i)
            
    dq = collections.deque(alist)
    dq.append(n+1)
    dq.appendleft(0)
    l = k+1
   


    while 1:
        if(len(dq)==0):
            break
        p = dq.popleft()
        q = dq.popleft()


        if p==0 and q==n+1:
            sum +=n//l
            if n%l>0:
                sum+=1
        elif p==0:
            le= q-1
            sum += le//l
        elif q==n+1:
            le = q-p-1
            sum +=le//l
        else:
            le = q-p-1
            le -= 2*k
            if le<=0:
                continue
            else:
                sum += le//l
            if le%l:
                sum+=1

    print(sum)


