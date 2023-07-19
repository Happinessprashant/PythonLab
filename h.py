# print("hello")

import multiprocessing

def test():
    print("This is the multiprocessing program")

if __name__ == '__main__':
    m = multiprocessing.Process(target=test)
    print("This is my Main program")
    m.start()
    m.join()


#


import multiprocessing
def sqr(n):
    return n**2


if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        out = pool.map(sqr , [1,2,3,4,5])
        print(out)