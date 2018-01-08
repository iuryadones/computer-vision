import multiprocessing as mp
import numpy as np

def sqrt(x):
    return np.sqrt(x)

if __name__ == '__main__':
    pool = mp.Pool()
    results = pool.map(sqrt, range(100))
    print(results)
