import math as mth
import time as tm
import multiprocessing as mp

def primos(n):
    arr = [True]*n
    # res = 0
    for i in range(n):
        if i < 2:
            arr[i] = False
        elif i > 2:
            for j in range(2, mth.ceil(mth.sqrt(i))+1):
                if i % j == 0:
                    arr[i] = False
                    break
        # if arr[i] == True:
            # res += i
    return arr

def primos_multi(n):
    if n < 2:
        return n, False
    elif n == 2:
        return n, True
    else:
        for j in range(2, mth.ceil(mth.sqrt(n)) +  1):
            if n % j == 0:
                return n, False
    return n, True

if __name__ == "__main__":
    # Single
    n = 5000000
    st = tm.time()
    res = primos(n)
    print(res[:30])
    en = tm.time()
    print("Tiempo single:", en-st)

    # multi
    st1 = tm.time()
    n_arr = range(n)
    n_process = 10
    with mp.Pool(processes=n_process) as pool:
        res = pool.map(primos_multi, n_arr)
    pool.close()
    print(res[:30])
    en1 = tm.time()
    print("Tiempo multi:", en1-st1)


print(primos(10))