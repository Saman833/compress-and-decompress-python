import random
for i in range (1,20):
    b=[[j,0] for j in range(0,128)]
    file=open("org_test"+str(i)+".txt","w")
    num_char=random.randint(100,1000)
    n=num_char
    for j in range (10,128):
        u=random.randint(-400,num_char) 
        b[j][1]=u
    for _ in range (10000000):
        if (len(b)<=10) :
            break
        x=random.randint(10,len(b)-1)
        if (b[x][1]>0) :
            b[x][1]-=1
            random_char=chr(b[x][0])
            file.write(random_char)
        else : 
            del b[x]
    file.close()
        