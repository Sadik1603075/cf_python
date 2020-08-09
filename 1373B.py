t = int(input())

for testcase in range(t):
    s = input()
    n = len(s)
    zero=0
    one =0
    for i in range(len(s)):
        if s[i]=='1':
            one+=1
        else:
            zero+=1
    if one==n or zero ==n:
        print('NET\n')
        continue
    else:
        one = min(zero,one)
        if one%2==1:
            print('DA\n')
        else:
            print('NET\n')