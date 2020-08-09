t = int(input())

for testcase in range(t):
    s = input()
    n = len(s)

    cur =0
    res=0
    arr=[0]*n
    for i in range(n):
        if s[i]=='-':
            if cur<0:
                arr[i]= i+1
            else:
                arr[i] = 1
            cur -=1
        else:
            if cur<0:
                arr[i] = i+1
                cur=1
            else:
                arr[i] =1
                cur+=1
    if cur<0:
        res += n
    for i in range(n):
        res+=arr[i]
    print(res,'\n')


    