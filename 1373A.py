
t = int(input())

while t>0 :
    t-=1
    a,b,c=map(int,input().split())
    s=""
    if(a>c): print('-1 ',b,'\n')
    elif(a==c and b==1): print('-1 -1\n')
    elif(a==c ): print('-1 ',b,'\n') 
    elif( b==1 and c>=a ): print('1 -1\n')
    elif( a*b<= c) :print('1 -1\n')
    else : print('1 ',b,'\n')

        