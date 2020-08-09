
t = int(input())
for testcase in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    for i in range(n):
        if i%2==0:
            arr[i] = abs(arr[i])*-1
        else:
            arr[i] = abs(arr[i])
        print(arr[i],end=" ")

    print()
        
    