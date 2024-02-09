import os
for i in range (1,20) : 
    file1 = os.stat("org_test"+str(i)+".txt")
    file2 = os.stat("compressed"+str(i)+".txt")
    print(file1.st_size,file2.st_size,(file2.st_size)/(file1.st_size))
for i in range(1,20):
    origianl_file=open("org_test"+str(i)+".txt","r")
    compressed_file=open("comp_test"+str(i)+".txt","r")
    ind=0
    while(True):
        ind=0
        c1=origianl_file.read(1)
        c2=compressed_file.read(1)
        if (not c1 and not c2):
            ind=1
            break
        elif ((not c1) or (not c2)) :
            ind=1
            break 
        if (c1!=c2):
            print(f"wrong ans in the test  {ind} + {c1} + {c2} test")
            ind=1
            break
    if (ind>0):
        print (f"test {i} is ok")
                
        
        