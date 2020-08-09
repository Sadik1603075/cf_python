t = int(input())

for testcase in range(t):
    n = int(input())
    s = input()
    ok=0
    indx=-1
    c=0
    s2=""
    s1=""

    for i in range(len(s)):
        if(s[i]=='0'):
            s2+="0"
            c+=1
        else:
            ok=1
            indx=i
            break
    if(ok == 0):
        print(s2+'\n')
        continue

    ok=0
    indx1=-1

    for i in reversed(range(len(s))):
        if s[i]=='1':
            s1+="1"
            c+=1
        else:
            ok=1
            indx1=i
            break

    if c==n:
        print(s2+s1+'\n')
        continue
    print(s2 +'0'+s1+'\n')






