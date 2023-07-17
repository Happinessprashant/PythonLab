
#                                  Custom Exception Handling

# raise:
# In Python, 
#       you can use the raise statement to raise an exception manually. 
#       This allows you to handle exceptional conditions or errors in your code. 
#       The raise statement requires an exception type and an optional error message.



# class validate_age(Exception):
#     def __init__(self, msg):
#         self.msg = msg


# def validate_age(age):
#     if age < 0:
#         raise validate_age("You have entered a negative age")
#     elif age > 200:
#         raise validate_age("You have entered a higher age")
#     else:
#         print("Age is valid")


# try:
#     age_str = input("Enter age: ")
#     age = int(age_str)
#     validate_age(age)
# except ValueError:
#     print("Error: Invalid input. Please enter a valid integer age.")
# except validate_age as e:
#     print("Error:", str(e))











class validate_age(Exception):
    
    def __init__(self,msg):
        self.msg = msg
        
        
def validate_age(age):
    
    if age<0:
        raise validate_age("You are Entered negative age")
    
    elif age>200:
        raise validate_age("You are Entered Higher age")   
    
    else:
        print("Age is Validate")
             
  
       
try:
    age=int(input("Enter age "))         
    validate_age(age) 

except validate_age as e:
    print(e)




print("==================================================")
