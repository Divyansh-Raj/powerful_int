intervals=[[1,4],[12,45],[3,8],[10,12]]
ka=3
count_x=0
d={}
flag=0
for i in intervals:
    for j in i:
        count_x=i.count(j)
        if j in d:
            d[j]=d[j]+count_x
        else:
            d[j]=count_x

v=list(d.values())
k=list(d.keys())
for i in v:
    if (i>=ka):
       flag=1
    else:
        v[v.index(i)]=0
if ( not flag):
    print(-1)
    exit()

ls=[]
start=-1
c=0
for i in range(len(v)):
    if (v.count(max(v)))<=1:
        print(k[v.index(max(v))])
        
        break
   
    else:
        ls.append(k[v.index(max(v),start+1)])
        start=v.index(max(v),start+1)
        c+=1
       
        if c==(v.count(max(v))):
            break
print(max(ls))

        




    

  

