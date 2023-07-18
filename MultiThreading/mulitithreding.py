
# multithreading:
# In Python, multithreading is a technique that allows multiple threads of 
# execution to run concurrently within a single process. Each thread represents
# a separate flow of control, executing instructions independently of other threads. 
# Multithreading is commonly used to perform multiple tasks concurrently, 
# improve performance, and enhance the responsiveness of applications.

import threading
def test(id):
    print("program start %d" %id)
# test(45)    

thread = [threading.Thread(target=test , args=(i ,))for i in range(10)]
for i in thread:
    i.start()
   
print(id(thread))
print(thread)