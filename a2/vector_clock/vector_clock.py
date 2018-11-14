class vector_clock(object):
    def __init__(self, id):
        self.id = id
        self.clocks = dict()
        self.clocks[self.id] = 0

    def recv(self, from_vector):
        for k, v in from_vector.clocks.items():
            if k not in self.clocks:
                self.clocks[k] = v
            else:
                self.clocks[k] = max(self.clocks[k], v)
        self.clocks[self.id] += 1

    def send(self, to_vector):
        self.clocks[self.id] += 1
        to_vector.recv(self)
    
    def do_work(self):
        self.clocks[self.id] += 1

    def print_clock(self):
        print(self.id, self.clocks)


if __name__=="__main__":
    # init 5 vector clocks for each process
    vcs = [vector_clock("P{}".format(id)) for id in range(1, 6)]
    
    # print vector clocks
    [vc.print_clock() for vc in vcs]
    print('='*50)
    
    vcs[2].send(vcs[1])
    vcs[1].send(vcs[0])
    vcs[1].send(vcs[2])
    vcs[0].send(vcs[1])
    vcs[2].send(vcs[0])
    vcs[1].send(vcs[2])
    vcs[2].send(vcs[0])

    # print vector clocks
    [vc.print_clock() for vc in vcs]
    print('='*50)

