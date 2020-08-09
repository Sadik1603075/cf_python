t = int(input())

for testcase in range(t):
    str = input()
    s=""
    n = len(str)

    if len(str)==2:
        print(str,'\n')
    else:
        for i in range(0,n,+2):
            s+=str[i]
        print(s+str[n-1],'\n')
