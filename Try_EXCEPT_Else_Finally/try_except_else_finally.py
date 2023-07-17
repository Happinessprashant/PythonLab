try:
    f=open("test.txt","r")
    b=2/0
except Exception as e:
    print("Hello",e)    
    
a=9+7
   
   
print("===============================================================================")  


try:
    f=open("test.txt","w")
    f.write("Hello")
except Exception as e :
    print("Exception is Occure",e)
    
else:
    f.close()
    print("File is Closed.....")    


print("===============================================================================")  


try:
    f=open("testq.txt","r")
    f.write("Hello")
finally:
    print("This is in the Finally Block")





print("===============================================================================")  



try:
    f=open("test.txt","w")
    f.write("Hello,Prashant")
except Exception as e :
    print("Exception is Occure",e)
    
finally:
    print("This is in the Finally Block")


print("===============================================================================")  

