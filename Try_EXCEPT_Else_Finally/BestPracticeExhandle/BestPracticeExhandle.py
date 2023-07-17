
import logging
logging.basicConfig(
    filename='error.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# logging.basicConfig(filename='error.log', level=logging.ERROR )
# , format='%(asctime)s - %(levelname)s - %(message)s' )
#use always a specific exception
# try:
#     10/0
    
# except Exception as e:
#         print(e) 
# print("================================")        
# try:
#     10/0
    
# except ZeroDivisionError as e:
#         print(e)                
# print("================================")         
        
#print always  a give proper message

try:
    10/0
    
except ZeroDivisionError as e:
    logging.error("It use the actual handle the divided by zero error {}".format(e))
    logging.shutdown()
    print("It use the actual handle the divided by zero error ",e)        
        
print("================================") 
        
        
        
#Document all error

#cleanup all the resources


try:
    with open("test.txt","w") as f :
        f.write("Hello")
    
except FileExistsError as e :
    logging.error("File error handle {}".format(e))
    print(e)     
        
finally:
    f.close()
    logging.shutdown()     