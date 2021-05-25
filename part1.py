# Import modules
import math
import time
import multiprocessing
from multiprocessing import Pool
from functools import partial

# Generate prime numbers function for first half of part 1
def prime_func_1(num, b):
    try:
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                print(i,"times",num//i,"is",num)
                print("Time:", time.time()-b)
                print("Task:", multiprocessing.current_process()) 
                break
        else:
            print(num,"is a prime number")
            print("Time:", time.time()-b)
            print("Task:", multiprocessing.current_process()) 
        print("")
    except Exception as e:
        print ('ERROR: %s' % e)
    return time.time() - b

# Generate prime numbers for second half of part 1 (used for plotting)
def prime_func_2(num, base):
    start = time.time() - base
    try:
        for i in range(2,num):
            if (num % i) == 0:
                break
    except Exception as e:
        print ('ERROR: %s' % e)
    stop = time.time() - base
    return start,stop

# Generate running time for each individual task in order to calculate average task running time
def prime_func_3(num, base):
    start = time.time() - base
    try:
        for i in range(2,num):
            if (num % i) == 0:
                break
    except Exception as e:
        print ('ERROR: %s' % e)
    stop = time.time() - base
    return stop - start

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

# Create list of large prime numbers
primes_list_1 = [15485867, 32452843, 32452867, 49979687, 49979693, 67867967, 67867979, 86028121, 86028157, 104395301, 104395303, 122949823, 122949829, 141650939, 141650963, 160481183, 160481219, 179424673]

# Run multiprocessing function with 1, 2, 3, and 4 cores - this will be ran inline in the Jupyter notebook
for i in range(1, 5):
    pool_process(prime_func_1, primes_list_1, i)
