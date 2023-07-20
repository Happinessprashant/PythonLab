
# def squre(index , value):
#     value[index] = value[index]**2
    
    
# l=[1,2,3,4,5]   
# squre(1 ,l)
# print(l)

import multiprocessing

def squre(index , value):
    value[index] = value[index]**2
    
    
if __name__ =='__main__':
    l=[1,2,3,4,5,6,7,8,9,10]
    arr = multiprocessing.Array('i',l) 
    process=[]
    
    for i in range(10):
        m=multiprocessing.Process(target=squre , args=(i, arr))
        process.append(m)
        m.start()
        
    for i in process:
        m.join()
        
    print(list(arr))        
        