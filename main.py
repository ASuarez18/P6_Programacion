from multiprocessing import Pool as pl
import time as tm

def convencional(n):
    res = 0
    if n < 2:
        return False
    else:
        for i in range(2, n):
            crec = 2
            primo = True
            while primo and crec < i:
                if i % crec == 0:
                    primo = False
                else:
                    crec += 1
            if primo:
                res += i

    return res
t = tm.time()
print("Suma:", convencional(500000), "\nTiempo:", tm.time() - t)
