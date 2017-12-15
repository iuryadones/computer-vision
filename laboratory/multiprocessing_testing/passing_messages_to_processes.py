import multiprocessing as mp


class MyFancyClass(object):
    
    def __init__(self, name):
        self.name = name

    def do_something(self):
        proc_name = mp.current_process().name
        print(f'Doing something fancy in {proc_name} for {self.name}!')

def worker(q):
    obj = q.get()
    obj.do_something()

if __name__ == '__main__':
    queue = mp.Queue()
    p = mp.Process(target=worker, args=(queue,))
    p.start()

    queue.put(MyFancyClass('Fancy Dan'))

    # wait for the worker to finish
    queue.close()
    queue.join_thread()
    p.join()

