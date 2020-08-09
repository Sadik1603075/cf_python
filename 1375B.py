import math
t = int(input())


for testcase in range(t):
    n,m = map(int,input().split())

    #grid=[[] for _ in range(n)] 
    #for i in range(n):grid[i] = [int(_) for _ in input().split()]
    grid =[]
    for i in range(n):
        a = list(map(int,input().split()))
        grid.append(a)
    ok=0
    for i in range(n):
        for j in range(m):
            if     i==0 and j==0 and grid[i][j]>2: ok =1
            elif i==n-1 and j==0 and grid[i][j]>2: ok =1
            elif i==n-1 and j==m-1 and grid[i][j]>2: ok =1
            elif i ==0  and j==m-1 and grid[i][j]>2: ok =1

            if i==0  and grid[i][j]>3: ok =1
            elif j==0 and grid[i][j]>3: ok=1
            elif i==n-1 and grid[i][j]>3: ok=1
            elif j==m-1 and grid[i][j]>3: ok=1
            elif grid[i][j]>4 : ok=1
            grid[i][j] = 4
    if ok==1:
        print('NO')
    else:
        print('YES')
        grid[0][0]=2
        grid[0][m-1]=2
        grid[n-1][0]=2
        grid[n-1][m-1]=2
        for i in range(1,m-1): grid[0][i]=3
        for i in range(1,m-1): grid[n-1][i]=3
        for i in range(1,n-1): grid[i][0]=3
        for i in range(1,n-1): grid[i][m-1]=3

        for i in range(n):
            for j in range(m):
                print(grid[i][j],end=" ")
            print()









    
