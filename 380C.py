import sys
sys.setrecursionlimit(10**6+10) 

maxl = 4000006
t = [0]*maxl
o = [0]*maxl
c = [0]*maxl

class Point:
    def __init__(self,t,o,c):
        self.t = t
        self.o = o
        self.c = c


def build( node, left,right ):
    if left==right:
        if s[left]=='(':
            o[node]=1
        else:
            c[node]=1
        return
    mid = (left+right)//2

    build(2*node,left,mid)
    build(2*node+1,mid+1,right)

    tmp = min(o[2*node],c[2*node+1])
    t[node] = t[2*node] + t[2*node+1] + tmp*2
    o[node] = o[2*node] + o[2*node+1] - tmp
    c[node] = c[2*node] + c[2*node+1] - tmp

    #print('Opening: ',o[node],'Closing: ',c[node],' range ',left,right,' sequence: ',t[node])


def query(node,left,right,x,y):
    
    if(right<x or left>y):
        ans =Point(0,0,0)
        return ans

    if( left>=x and right<=y):
        ans =Point(t[node],o[node],c[node])
        return ans


    mid = (left+right)//2
    p = Point(0,0,0)
    q = Point(0,0,0)
    p = query(2*node,left,mid,x,y)
    q = query(2*node+1,mid+1,right,x,y)

    zt = p.t + q.t
    tmp = min(p.o,q.c)

    zt += tmp*2
    zo = p.o + q.o -tmp
    zc = p.c + q.c - tmp
    z = Point(zt,zo,zc)
    return z

if __name__ == "__main__":    
    s = input()
    n = len(s)-1
    build(1,0,n)
    m = int(input())

    for i in range(m):
        u,v = map(int,input().split( ))
        ans =  Point(0,0,0)
        ans= query(1,0,n,u-1,v-1)
        print(ans.t)

