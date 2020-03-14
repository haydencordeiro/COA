def f(nl,l):#returns the page which came first the input list(FCFS)
    fmin=1000
    for i in nl:
        if l.index(i)<fmin:
            fmin=l.index(i)
    return(l[fmin])



def smal(cl,l,fl):#returns the page in the cache list that has to be replaced
    ind=0
    val=0
    nl=[]#if and page doesnt exist in the future it gets appended in this list
    for i in cl:

        try:
            if(l.index(i)>ind):
                ind=l.index(i)
                
        except:
            nl.append(i)


    if len(nl)==0:#if all page exist in the future
        val=l[ind]
        return(val)
    else:#if one or more page exist in the future
        return f(nl,fl)


sl=list(map(int,input().split()))#pages input list
# sl=[2, 3,2, 1, 5, 2, 4, 5, 3, 2, 5, 2]
slt=sl#copy of the pages list
cl=[]#frame list(cache list)
hm=[]#hit and miss appends h and m respectively

frm=int(input('enter no of pages'))-1#the frame size
print(slt)
for i in slt:#goes through every page
    ask=input('y/n').lower().strip()#ask the user if they want to continue
    if ask=='n':
        break
    print(i)
    if len(cl)<=frm: #if the cache list is not full
        if i not in cl:
            cl.append(i)
            print('miss')
            hm.append('m')
        elif i in cl:
            print('hit')
            hm.append('h')

    else:#if the cache list is full
        if i in cl:
            print('hit')
            hm.append('h')
        if i not in cl:
            print('miss')
            hm.append('m')
            r=smal(cl,slt,sl)
            cl[cl.index(r)]=i

    if len(cl)==frm+1:
        print(*cl)
    else:
        t=frm+1-len(cl)
        print(*cl,end="")
        for i in range(t):
            print('-1',end="")
        print()
 

    slt=slt[1:]


print('total hits',hm.count('h'))
print('total miss',hm.count('m'))
print('Hit ratio',(hm.count('h')/len(hm)*100))
print('miss ratio',(hm.count('m')/len(hm)*100))