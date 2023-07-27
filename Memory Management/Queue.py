import multiprocessing

# def producer(q):
#     for i in ["Sudh","kumar", "asd"]:
#         q.put(i)


# def consume(q):
#     while True:
#         item = q.get()
#         if item is None:
#             break
        
#         print(item)

# if __name__ == "__main__":
#     queue = multiprocessing.Queue()
#     m1 = multiprocessing.Process(target=producer , args=(queue,))
#     m2 = multiprocessing.Process(target=consume , args=(queue ,))
    
#     m1.start()
#     m2.start()
#     queue.put("Prashant")  
#     m1.join()
#     m2.join()
        
# def producer(q):
#     for i in ["Sudh","kumar", "asd","abcd"]:
#         q.put(i)


# def consume(q):
#     while True:
#         item = q.get()
#         if item is None:
#             break
#         print(item)

# if __name__ == "__main__":
#     queue = multiprocessing.Queue()
#     m1 = multiprocessing.Process(target=producer , args=(queue,))
#     m2 = multiprocessing.Process(target=consume , args=(queue ,))
    
#     queue.put("1")  
#     m1.start()
#     m2.start()
#     queue.put("Prashant")  
#     m1.join()
#     queue.put("Jadhav")  
#     m2.join()
#     queue.put("Mangoli")  

# def producer(q):
#     for i in range(10):
#         q.put(i)


# def consume(q):
#     while True:
#         item = q.get()
#         if item is None:
#             break
#         print(item)

# if __name__ == "__main__":
#     queue = multiprocessing.Queue()
#     print(type(queue))
#     m1 = multiprocessing.Process(target=producer , args=(queue,))
#     m2 = multiprocessing.Process(target=consume , args=(queue ,))
    
#     list=[m1,m2]
#     queue.put("1")  
#     for i in list:
#         i.start()
#         i.join()
#         queue.put("Prashant") 
#     # m1.start()
#     # m2.start()
#     # queue.put("Prashant")  
#     # m1.join()
#     # queue.put("Jadhav")  
#     # m2.join()
#     # queue.put("Mangoli")  
 
 
 
 
        