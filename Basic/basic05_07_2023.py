#!/usr/bin/env python
# coding: utf-8

# In[1]:


number = int(input("Enter Number "))
counter=0
a,b=0,1
for i in range(number):
    print(a)
    c=a+b
    a=b
    b=c
    counter+=1


# In[6]:


a="prashant"

len(a)
# for i in range(len(a),-1,-1):
#     print(i)


# In[16]:


for i in range(len(a)-1,-1,-1):
    print(a[i],end="")


# In[21]:


a="prashanrt"
rev=""
l=len(a)
while(0<l):
    rev= rev+a[l-1]
    l-=1
print(rev)    
    


# In[24]:


for i in range(1,len(a)+1):
    print(a[-i])


# In[25]:


for i in range(1,len(a)+1):
    print(a[-i],end="")


# In[26]:


num=int(input("enter number"))
i=1
while(i<=10):
    print(i*num)
    i+=1
    


# In[28]:


num=int(input("enter number"))
i=1
while(i<=10):
    print(i,"*",num," = ",i*num)
    i+=1


# In[33]:


num=int(input("enter number"))
for i in range(1,11,1):
    print(i*num)


# In[34]:


num=int(input("enter number"))
for i in range(1,11,1):
    print(i,"*",num," = ",i*num)


# In[37]:


# while_else
# when while loop is completed then the else loop is executed 

n=5
i=1

while(i<n):
    print(i)
    i+=1
else:
    print("Else bolck is executed when the while loop is executed successful")


# In[38]:


n=5
i=1

while(i<n):
    print(i)
    if i==3:
        break
    i+=1
else:
    print("Else bolck is executed when the while loop is executed successful")


# In[40]:


n=5
i=1

while(i<n):
    print(i)
    if i==3:
        break
    i+=1
else:
    print("Else bolck is executed when the while loop is executed successful")


# In[1]:


n=5
i=1

while(i<n):
    print(i)
    i+=1
    if i==3:
        continue     
else:
    print("Else bolck is executed when the while loop is executed successful")


# In[4]:


l=[1,2,3,4,5]
l1=[]
for i in l:
    l1.append(i**2)

print(l1)    


# In[5]:


# List Comprehension imp
[i**2 for i in l]


# In[7]:


# Even Numbers
[i for i in l if i%2==0]


# In[10]:


# Odd Numbers
[j for j in l if j%2==1]


# In[14]:


l3=["prashant","jadhav","mangoli"]


# In[15]:


[i.upper() for i in l3 ]


# In[17]:


[i.title()  for i in l3]


# In[18]:


[i.lower() for i in l3]


# In[19]:


# Tupple  Comprehension


# In[21]:


list(i**2 for i in l)


# In[22]:


# Dictionary  Comprehension


# In[23]:


d={"kay1":1, "kay2":2,"kay3":3, "kay4":4} 


# In[24]:


d.items()


# In[25]:


{k:v**2 for k, v in d.items()}


# In[26]:


{k:v for k,v in d.items() if v>1}


# In[33]:


print("Even" , {k:v for k,v in d.items() if v%2==0})


# In[32]:


print("Odd",{k:v for k,v in d.items() if v%2==1})


# In[37]:


l4=[[1,2,3],[2,3,4],[3,4,5]]


# In[45]:


for i,j,k in l4:
       print("i = ",i,end=" ")
       print("j = ",j,end=" ")
       print("k = ",k)


# In[48]:


print("Secound value(j) of the divisible by 2 => ",[[i,j,k] for i ,j,k in l4 if j%2==0])


# In[52]:


print("Addition of values (i+j+k)  => ",[[i,j,k] for i ,j,k in l4 if (i+j+k)>7])


# In[59]:


# Functions 

l=[1, 2, 3, 4, 5]

print("print",l)
print("type",type(l))
print("len",len(l))
    


# In[60]:


# Functions 
  
#     def function_name():
#         Body of Function
#              pass:->
#                 keyword is used to the empty block of function


# calling function :=
#        function_name()
        
# Example :
      
# def test(): //function Declared 
#     pass // (function Body) pass is used to the only decared then use
        

# test() // function calling



        


# In[61]:


def test():
    pass


test()


# In[64]:


def test1():
    print("prashant")
    
test1()    


# In[65]:


# print statement gives only NontType of the that type


# In[70]:


def test2():
    return "Prashant "


# In[67]:


test2()


# In[72]:


test2()+" jadhav"


# In[73]:


test2()+2


# In[75]:


def test3():
    return 8
test3()

test3()+9


# In[ ]:




