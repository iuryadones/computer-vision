import multiprocessing as mp
import numpy as np


def sqrt(x):
    return np.sqrt(x)


if __name__ == '__main__':
    pool = mp.Pool(16)
    results = [pool.apply_async(sqrt, (x,)) for x in range(100)]
    roots = [r.get() for r in results]
    print(roots)
