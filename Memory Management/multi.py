

import multiprocessing
# def sqr(n):
#     return n**2

# if __name__ == "__main__":
#     with multiprocessing.Pool(processes=4) as pool:
#         out = pool.map(sqr , [1,2,3,4,5])
#         print(out)
        
        
        
        
        
# #    ////////////////////////////
        
       


def producer(q):
    for i in range(10):
        q.put(i)


def consume(q):
    while True:
        item =q.get()
        if item is None:
            print(item)


# if __name__ == "__main__":
#     with multiprocessing.Pool(processes=4) as pool:
#         out = pool.map(sqr, [1, 2, 3, 4, 5])
#         print(out)
     
        