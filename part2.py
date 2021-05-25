# Import modules
import math
import time
import multiprocessing
from multiprocessing import Pool
from functools import partial
import random

# Function to sum a list of variable length, filled with integers in the range of 10000 - 20000
def randomSum_func_1(length, b):
    try:
        sum = 0
        randomList = [random.randint(10000,20000) for x in range(length)]
        for element in randomList:
            sum += element
        print(sum,"is the sum of a random list of {} numbers in the range of 10000-20000".format(length))
    except Exception as e:
        print ('ERROR: %s' % e)
    print("Time:", time.time()-b)
    print("Task:", multiprocessing.current_process()) 
    print("")
    return time.time() - b

# Used for second half of part 2 (plotting)
def randomSum_func_2(length, base):
    start = time.time() - base
    try:
        sum = 0
        randomList = [random.randint(10000,20000) for x in range(length)]
        for element in randomList:
            sum += element
    except Exception as e:
        print ('ERROR: %s' % e)
    stop = time.time() - base
    return start,stop

# Used for averaging running times for individual tasks
def randomSum_func_3(length, base):
    start = time.time() - base
    try:
        sum = 0
        randomList = [random.randint(10000,20000) for x in range(length)]
        for element in randomList:
            sum += element
    except Exception as e:
        print ('ERROR: %s' % e)
    stop = time.time() - base
    return stop-start

# Multiprocessing function
def pool_process(f, data, pool_size = multiprocessing.cpu_count()):
    if __name__ == '__main__':
        with multiprocessing.get_context('spawn').Pool(processes=pool_size) as pool:
            tpl = time.time()
            print(data, pool_size)
            
            result = pool.map(partial(f, b=tpl), data)
            pool.close()
            pool.join()
            print("Results", result)
            print("Overall Time:", int(time.time() - tpl))
            print("______________________________________________________")
            return result

# Create list of 20 large integers
randomSum_list_1 = [x for x in range(1000000, 1000020)]

# Tests multiprocessing capabilities inline in the Jupyter notebook (1, 2, 3, and 4 processors)
for i in range(1, 5):
    pool_process(randomSum_func_1, randomSum_list_1, i)