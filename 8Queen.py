import copy
import random
class queen():  
    depth:int
    table : list
    def __init__(self,depth=0,table=[]):
        self.depth=depth
        self.table=table
    def check(self,n):
        b=True
        if self.depth==0:
            if n in range(0,8):
                return True   
        else:   
            for q in range(0,self.depth):        
                if self.table[q]==n or abs(self.depth-q)==abs(n-self.table[q]): 
                    return False   
            return True
        
class board:
    possible : list
    def __init__(self,possible=[]):
        self.possible=possible                 
    def createTable(self,q):     
        while(q.table[7]==-1):
            for i in range(0,8):
                if q.check(i):                    
                    g=queen()
                    g=copy.deepcopy(q)
                    g.table[g.depth]=i
                    g.depth=g.depth+1
                    self.createTable(g)                   
            if q.table[q.depth]==-1:
                return                   
        self.possible.append(q.table)
 
def sum(a,dic):
    s=0
    for i in range(len(a)):
        s=dic[(i,a[i])]+s        
    return s
          
h=[-1,-1,-1,-1,-1,-1,-1,-1]
qu=queen(0,h)
b=board()
b.createTable(qu)
q={}
h=0
mm=0
for c in range(0,8):
    for v in range(0,8):       
        q[(c,v)]=random.randint(1, 99)
print("numbers:")
for item in q:
    print(item,q[item])
print("------------------")
print("way to place queens and their weight:")


finallist=[]
for f in b.possible:
    finallist.append((f,sum(f,q)))
y=[]
for item in finallist: 
    print(item) 
    if mm<=item[1]:
        mm=item[1]
print("------------------")
print("Final Solution:")
for it in finallist:
    if mm==it[1]:
        print(it)
input()
    
                  

        
        
