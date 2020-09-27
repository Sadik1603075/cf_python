def summation(v):
    local_max=-1000000000+7

    global_max=-1000000000+7

    for i in range(len(v)):
        local_max=max(v[i],local_max+v[i])
        global_max=max(local_max,global_max)

    return global_max


if __name__ == "__main__":

    testcase = int(input())
    for test in range(testcase):
        n = int(input())
        arr = list(map(int,input().split()))
        suma=0
        for i in range(n):
            if i%2==0:
                suma= suma + arr[i]
        v1=[]
        v2=[]
        
        for i in range(0,n-1,2):
            v1.append(arr[i+1]-arr[i])
        for i in range(1,n-1,2):
            v2.append(arr[i]-arr[i+1])
        x = summation(v1)
        y = summation(v2)
        m = max(x,y)
        m = max(m,0)
        print(suma+m)




