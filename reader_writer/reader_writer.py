import threading
import time

class Reader(threading.Thread):
    def __init__(self, Number):
        threading.Thread.__init__(self)
        self.Number = Number
    
    def run(self):
        self.Number.read()

class Writer(threading.Thread):
    def __init__(self, Number):
        threading.Thread.__init__(self)
        self.Number = Number
    
    def run(self):
        self.Number.write(5)

class Number(object):
    def __init__(self, start=99):
        self.lock = threading.Lock()
        self.value = start
    
    def write(self, value):
        try:
            self.lock.acquire()
            print('Writer acquired the lock.')
            self.value = value
            print('Set value to {}.'.format(self.value))
        except Exception as e:
            print(e)
        finally:
            print('Writer released the lock.')
            self.lock.release()

    def read(self):
        try:
            self.lock.acquire()
            print('Reader acquired the lock.')
            print('Value currently equals {}.'.format(self.value))
        except Exception as e:
            print(e)
        finally:
            print('Reader released the lock.')
            self.lock.release()
        

if __name__=='__main__':
    start = time.time()
    for _ in range(55000):
        number = Number()
        reader1 = Reader(number)
        reader2 = Reader(number)
        writer = Writer(number)

        reader1.start()
        writer.start()
        reader2.start()

        reader1.join()
        reader2.join()
        writer.join()

    print("Runtime = {}".format(time.time() - start))
    print('Main terminating')