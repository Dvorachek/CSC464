import random


ORDERS = ('ATTACK', 'RETREAT')
STATUS = ('TRAITOR', 'LOYAL')
GENERALS = []  # Keep 
N = 7  # change number of total generals
NUM_TRAITORS = 2  # number of traitor generals
M = 3  # nuber of rounds of 'recursion'


class general(object):
    def __init__(self, id, faction):
        self.id = id  # 0 is the commander
        self.faction = faction  # loyal or traitor

        self.rounds = dict()
        for round in range(M+1):
            self.rounds[round] = dict()
            for gen in range(N):
                self.rounds[round][gen] = []

        if self.id == 0:
            self.order = random.randint(0, 1)  # commander randomly generates order
            print "Commander's order: {}".format(ORDERS[self.order])  # for my reference
        else:
            self.order = 1
    
    def decide(self):
        l = [max(set(self.rounds[i][self.id]), key=self.rounds[i][self.id].count) for i in range(M+1)]
        self.order = max(set(l), key=l.count)

    def get_order(self, target_id):
        if self.faction == 0 and target_id % 2 == 0:
            return (self.order + 1) % 2
        else:
            return self.order

    def send_orders(self, round):
        for j in range(N):
            if j != self.id:
                self.rounds[round][self.id].append(GENERALS[j].get_order(self.id))


def create_generals():
    alliance = [0 if i < NUM_TRAITORS else 1 for i in range(N)]
    random.shuffle(alliance)
    return [general(i, alliance[i]) for i in range(N)]

# iterative approach
def consensus():
    # step 1
    for i in range(1, N):
        GENERALS[i].order = GENERALS[0].get_order(i)

    # step 2
    for round in range(M+1):
        for j in range(1, N):
            GENERALS[j].send_orders(round)

    # step 3
    for i in range(1, N):
        GENERALS[i].decide()


def vote():
    s = sum([gen.order for gen in GENERALS])
    if s < N/2.0:
        results = ORDERS[0]
    else:
        results = ORDERS[1]

    print 'factions: ',
    print ''.join("{} ".format(STATUS[gen.faction]) for gen in GENERALS)
    print 'votes: ',
    print ''.join("{} ".format(ORDERS[gen.order]) for gen in GENERALS)
    print("Commander status: {}".format(STATUS[GENERALS[0].faction]))
    print("Overall consensus: {} at dawn!".format(results))

    return STATUS[GENERALS[0].faction], results, ORDERS[GENERALS[0].order]


def test_output(results):
    consensus_command_loyal = 0
    command_loyal = 0

    for result in results:
        if result[0] == 'LOYAL':
            command_loyal += 1
            if result[1] == result[2]:
                consensus_command_loyal += 1

    print "{} / {} of times loyal command was obeyed".format(consensus_command_loyal, command_loyal)


if __name__=='__main__':
    random.seed(13)
    test_results = []  # will contain a tuple (general faction, final vote, general order)

    # do everything 10 times
    for _ in range(10):
        GENERALS = create_generals()

        consensus()

        test_results.append(vote())

        # reset for each iteration
        GENERALS = []
        print '='*50
    
    test_output(test_results)
