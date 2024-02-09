class character: 
    def __init__(self,what):
        self.number=1
        self.what=what
        self.code=""
    def update_number(self):
        self.number+=1
class Huffman_vertex :
    def __init__ (self,element,sum_el):
        self.num_el=1
        self.sum_el=sum_el
        self.subarry=[element]
        self.right_side=element
def change_char(saved_chars,initial_Fname,compressed_Fname,any_char,last_ind): 
    file2=open(compressed_Fname,"w")
    file=open(initial_Fname,"r")
    base_power=32
    char_num=64
    times=0
    for i in range(1,last_ind):
        file2.write(any_char[i].what+any_char[i].code+"\n")
    file2.write("end\n")
    while (True): 
        line=file.readline()
        if not line : 
            break
        for i in line : 
            u=saved_chars[i]
            for j in any_char[u].code:
                char_num+=int(j)*base_power
                times+=1
                base_power//=2
                if (base_power<=0): 
                    file2.write(chr(char_num))
                    char_num=64
                    base_power=32
    if (times%6):
        file2.write(chr(char_num))
    file2.close()
def merg_sort(l:int,r:int ,any_char,any_char_C):
    if (l+1>=r) :
        return 
    mid=(l+r)//2
    mid=int(mid)
    merg_sort(int(l),int(mid),any_char,any_char_C)
    merg_sort(int(mid),int(r),any_char,any_char_C)
    ind,left_i,right_i=l,l,mid
    while (ind<r):
        if (left_i>=mid):
            any_char_C[ind]=any_char[right_i]
            right_i+=1
        elif (right_i>=r):
            any_char_C[ind]=any_char[left_i]
            left_i+=1
        elif (any_char[left_i].number<=any_char[right_i].number):
            any_char_C[ind]=any_char[left_i]
            left_i+=1
        else :
            any_char_C[ind]=any_char[right_i]
            right_i+=1
        ind+=1 
    for i in range(l,r):
        any_char[i]=any_char_C[i]       
    return 
def Huffman_greedy(l,r,Huffman_vertexes,any_char):
    while (l+1<r):
        if (Huffman_vertexes[l].sum_el>Huffman_vertexes[l+1].sum_el):
            Huffman_vertexes[l],Huffman_vertexes[l+1]=Huffman_vertexes[l+1],Huffman_vertexes[l] # good way to change two things in python
        if (Huffman_vertexes[l].right_side>Huffman_vertexes[l+1].right_side):
            for i in range (Huffman_vertexes[l+1].num_el):
                any_char[Huffman_vertexes[l+1].subarry[i]].code+='0'
            for i in range (Huffman_vertexes[l].num_el):
                any_char[Huffman_vertexes[l].subarry[i]].code+='1'
            Huffman_vertexes[l+1].right_side=Huffman_vertexes[l].right_side
        else : 
            for i in range (Huffman_vertexes[l+1].num_el):
                any_char[Huffman_vertexes[l+1].subarry[i]].code+='1'
            for i in range (Huffman_vertexes[l].num_el):
                any_char[Huffman_vertexes[l].subarry[i]].code+='0'
        Huffman_vertexes[l+1].subarry.extend(Huffman_vertexes[l].subarry)
        Huffman_vertexes[l+1].num_el+=Huffman_vertexes[l].num_el
        Huffman_vertexes[l+1].sum_el+=Huffman_vertexes[l].sum_el
        for i in range(l+1,r-1):
            if (Huffman_vertexes[i].sum_el>Huffman_vertexes[i+1].sum_el):
                Huffman_vertexes[i],Huffman_vertexes[i+1]=Huffman_vertexes[i+1],Huffman_vertexes[i]
            else : 
                break
        l+=1
    for i in range(1,r):
        s="".join(reversed(any_char[i].code))
        any_char[i].code=s
def compress(initial_Fname,compressed_Fname): 
    any_char=[0] # here we will save all of the classes of character (for each char in file)
    # we will save it's char and how many times it occurs in the initial file 
    last_ind=int(1)
    saved_chars={}
    file=open(initial_Fname,"r")
    while (True): 
        line=file.readline()
        if not line:
            break
        for i in line: 
          if (i in saved_chars) :
               any_char[saved_chars[i]].number+=1
          else :
              saved_chars[i]=last_ind
              any_char.append(character(i))
              last_ind+=1
    any_char_C=any_char.copy()
    merg_sort(1,last_ind,any_char,any_char_C)
    for i in range (1,last_ind) :
        saved_chars[any_char[i].what]=i
    Huffman_vertexes=[0]
    for i in range(1,last_ind): 
        Huffman_vertexes.append(Huffman_vertex(i,any_char[i].number))
    Huffman_greedy(1,last_ind,Huffman_vertexes,any_char)
    change_char(saved_chars,initial_Fname,compressed_Fname,any_char,last_ind)
def decompress(compressed_Fname,goal_Fname):
    file=open(compressed_Fname,"r")
    file2=open(goal_Fname,"w")
    last_ind=0
    any_char=[]
    saved_codes={}
    while (True) :
        line=file.readline()
        if not line :
            print("Error : it is not a correct compressed file")
            return
        if (line=="\n"):
            line=str('\n'+file.readline())
        if (line=="end\n"):
            break
        any_char.append(character(line[0]))
        any_char[last_ind].code=line[1:].strip()
        saved_codes[any_char[last_ind].code]=any_char[last_ind].what
        last_ind+=1
    current_code=""
    while(True):
        c=file.read(1) #reads each char in the file one by one
        if not c :
            break
        k=ord(c)
        k-=64
        base_power=32
        while (base_power>0):
            if (k>=base_power):
                k-=base_power
                current_code+='1'
            else :
                current_code+='0'
            base_power//=2
            if (current_code in saved_codes):
                file2.write(saved_codes[current_code])
                current_code=""
    file.close()
    file2.close()
def read_files_for_compressing():
    for i in range (1,20): 
        initial_Fname="org_test"+str(i)+".txt"
        compressed_Fname="compressed"+str(i)+".txt"
        compress(initial_Fname,compressed_Fname)
def read_files_for_decompressing ():
    for i in range (1,20): 
        compressed_Fname="compressed"+str(i)+".txt"
        decompressed_Fname="comp_test"+str(i)+".txt"
        decompress(compressed_Fname,decompressed_Fname)
check_the_option=input("chosse one of the two options : \n  'c'  for compress \n  'd' for decompress\n")
if check_the_option.strip()=='c':
    read_files_for_compressing()
elif check_the_option.strip()=='d':
    read_files_for_decompressing()
else : 
    print("your choosen option is not recognize")
    
                
            
            
            
             
            
        