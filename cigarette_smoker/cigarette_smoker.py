import threading
import time
import random

class Locks(object):
    def __init__(self):
        self.lock_t = threading.Lock()
        self.lock_p = threading.Lock()
        self.lock_m = threading.Lock()
        self.lock_a = threading.Lock()
        self.lock = threading.Lock()

        self.lock_t.acquire()
        self.lock_p.acquire()
        self.lock_m.acquire()
        self.lock_a.acquire()

class Tobacco(threading.Thread):
    def __init__(self, Locks):
        threading.Thread.__init__(self)
        self.Locks = Locks
        self.daemon = True
    
    def run(self):
        while(True):
            self.Locks.lock_t.acquire()
            self.Locks.lock.acquire()
            print('Tobacco smoker picks up the paper and match.')
            self.Locks.lock_a.release()
            self.Locks.lock.release()

class Paper(threading.Thread):
    def __init__(self, Locks):
        threading.Thread.__init__(self)
        self.Locks = Locks
        self.daemon = True
    
    def run(self):
        while(True):
            self.Locks.lock_p.acquire()
            self.Locks.lock.acquire()
            print('Paper smoker picks up the tobacco and match.')
            self.Locks.lock_a.release()
            self.Locks.lock.release()

class Match(threading.Thread):
    def __init__(self, Locks):
        threading.Thread.__init__(self)
        self.Locks = Locks
        self.daemon = True
    
    def run(self):
        while(True):
            self.Locks.lock_m.acquire()
            self.Locks.lock.acquire()
            print('Match smoker picks up the tobacco and paper.')
            self.Locks.lock_a.release()
            self.Locks.lock.release()

class Agent(threading.Thread):
    def __init__(self, Locks):
        threading.Thread.__init__(self)
        self.Locks = Locks

    def run(self):
        #CHANGE ITERATIONS HERE
        for i in range(55000):
            self.Locks.lock.acquire()

            rn = random.randrange(0, 3)

            if rn == 0:
                print('Agent places tobacco and paper on the table.')
                self.Locks.lock_m.release()
            if rn == 1:
                print('Agent places tobacco and a match on the table.')
                self.Locks.lock_p.release()
            if rn == 2:
                print('Agent places a match and paper on the table.')
                self.Locks.lock_t.release()
            self.Locks.lock.release()
            self.Locks.lock_a.acquire()


if __name__=='__main__':
    start = time.time()

    locks = Locks()
    tobacco = Tobacco(locks)
    paper = Paper(locks)
    match = Match(locks)
    agent = Agent(locks)

    agent.start()

    tobacco.start()
    paper.start()
    match.start()

    agent.join()
    print("Runtime = {}".format(time.time() - start))
    print('Main terminating')