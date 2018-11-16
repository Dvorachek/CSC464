import sys


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


def print_results(ids, expected_results, vcs):
    print("Test results for {}".format(sys._getframe(1).f_code.co_name))
    print("Vector clocks ('id', {clock}):")
    [vc.print_clock() for vc in vcs]
    for i in range(len(vcs)):
        print("{}: expected result: {}; actual result: {}".format(ids[i], expected_results[i], vcs[i].clocks[ids[i]]))
    print('='*50)

def test_1():
    # init 3 vector clocks
    ids = ["P{}".format(id) for id in range(3)]
    vcs = [vector_clock(id) for id in ids]
    expected_results = [4, 5, 5]  # from following operations

    vcs[2].send(vcs[1])  # P2 sends to P1
    vcs[1].send(vcs[0])  # P1 sends to P0
    vcs[1].send(vcs[2])  # P1 sends to P2
    vcs[0].send(vcs[1])  # P0 sends to P1
    vcs[2].send(vcs[0])  # P2 sends to P0
    vcs[1].send(vcs[2])  # P1 sends to P2
    vcs[2].send(vcs[0])  # P2 sends to P0

    print_results(ids, expected_results, vcs)

def test_2():
    ids = ["P{}".format(id) for id in range(4)]
    vcs = [vector_clock(id) for id in ids]
    expected_results = [3, 10, 9, 2]

    vcs[1].send(vcs[0])  
    [vcs[1].do_work() for _ in range(8)]
    [vcs[2].do_work() for _ in range(8)]
    vcs[2].send(vcs[3])
    vcs[3].send(vcs[0])
    vcs[0].send(vcs[1])

    print_results(ids, expected_results, vcs)


if __name__=="__main__":
    test_1()
    test_2()
