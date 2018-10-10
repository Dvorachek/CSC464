import threading

class Locks(object):
    def __init__(self):
        self.lock = threading.Lock()

class Client(threading.Thread):
    def __init__(self, locks, id, server):
        threading.Thread.__init__(self)
        self.locks = locks
        self.id = id
        self.server = server
    
    def run(self):
        self.locks.lock.acquire()
        print("\nClient: My ID is {}".format(self.id))
        self.server.in_service = self.id
    
class Worker(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
        self.daemon = True
    
    def run(self):
        print("\nWorker: Hello {}".format(self.id))

class Server(threading.Thread):
    def __init__(self, Locks):
        threading.Thread.__init__(self)
        self.locks = Locks
        self.in_service = -1
        self.previous = -1
        self.daemon = True
    
    def run(self):
        while(True):
            if self.in_service != self.previous:
                self.previous = self.in_service
                worker = Worker(self.previous)
                worker.start()
                self.locks.lock.release()

    
if __name__=='__main__':
    locks = Locks()
    server = Server(locks)
    server.start()

    clients = [Client(locks, id, server) for id in range(5)]
    [client.start() for client in clients]
    [client.join() for client in clients]
    
    print('\nMain exiting')
