t = int(input())

for testcase in range(t):
    n = int(input())
    ok=0
    zor=0
    bizor=0

    arr = list(map(int,input().split()))

    for i in range(n):
        if(i%2==arr[i]%2):
            ok+=1
            continue
        if arr[i]%2==0:
            zor+=1
        else:
            bizor+=1
    if ok==n:
        print('0\n')
    else:
        if(zor==bizor):
            print(zor,'\n')
        else:
            print('-1\n')
