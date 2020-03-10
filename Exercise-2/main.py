f1=open('all_inputs.txt','r')
f2=open('indexd.txt','w')
while(True):
    f2.write(str(f1.tell())+' ')
    w=f1.readline()
    if(w!=''):
        f2.write(w.split()[1]+'\n')
    else:
        f1.close()
        f2.close()
        break
import time
t1=time.time()
q=int(input("enter roll: "))
f3=open('indexd.txt','r')
x=f3.readline().split()
while(True):
    if(int(x[1])==q):
        f4=open('all_inputs.txt','r')
        f4.seek(int(x[0]))
        t2=time.time()
        print('time',t2-t1)
        print(f4.readline())
        f3.close()
        f4.close()
        break
    else:
        x=f3.readline().split()
fn=[]
for i in range(1,101):
    fn.append('f'+str(i)+'.txt')
def partition(arr,low,high):
    i = ( low-1 )        
    pivot = arr[high][1]    
 
    for j in range(low , high):
 
        if   arr[j][1] <= pivot:
         
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
 
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )
 
def quickSort(arr,low,high):
    if low < high:
 
       
        pi = partition(arr,low,high)
 
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)



aq=open('indexd.txt','r')
lf=fn
ind=0
pp=[]
for i in range(1000000):
    q=aq.readline().split()
    q[1]=int(q[1])
    pp.append(q)
    if(len(pp)==10000):
        n = len(pp)
        quickSort(pp,0,n-1)
        f1=open(lf[ind],'w')
        for i in range(10000):
            pp[i][1]=str(pp[i][1])
            stri=''+' '.join(pp[i])
            f1.write(stri)
            f1.write('\n')
        f1.close()
        pp=[]
        ind=ind+1
we=open('sortind.txt','w')
p=[]
for i in fn:
    f=open(i,'r')
    p.append(f)
#p=[a,b,c,d,e,f,g,h,i,j]
o=[]
sm=[]
for i in range(len(p)):
    o.append(p[i].readline().split())
    sm.append(int(o[i][1]))
while(True):
    if(len(p)!=0):
        mi=sm.index(min(sm))
        we.write(' '.join(o[mi]))
        we.write('\n')
        o[mi]=p[mi].readline().split()
        if([]!=o[mi]):
            sm[mi]=int(o[mi][1])
        elif([]==o[mi]):
              p[mi].close()
              p.remove(p[mi])
              o.remove(o[mi])
              sm.remove(sm[mi])
    else:
        we.close()
        break
import time
t1=time.time()
x = int(input("enter roll: "))
l,r=0,999999
while l <= r:
    a=''
    mid = l + (r - l)//2
    f11=open('sortind.txt','r')
    for i in range(mid-1):
        f11.readline()
    a=f11.readline().split()
    if (int(a[1]) == x):
        t2=time.time()
        f12=open('all_inputs.txt','r')
        f12.seek(int(a[0]))
        print(f12.readline())
        print('time',t2-t1)
        f12.close()
        break
    elif int(a[1]) < x:
        l = mid + 1
    else:
        r = mid - 1
f11.close()

