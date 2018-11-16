import random


class general(object):
    def __init__(self, id, faction):
        self.id = id  # 0 is the commander
        self.faction = faction  # loyal or traitor
        self.orders_recieved = []
        self.path = []

        self.rounds = dict()
        for round in range(m+1):
            self.rounds[round] = dict()
            for gen in range(n):
                self.rounds[round][gen] = []

        if self.id == 0:
            self.order = random.randint(0, 1)  # commander randomly generates order
            print "Commander's order: {} {}".format(self.order, orders[self.order])  # for my reference
            self.orders_recieved.append(self.order)
        else:
            self.order = 1
    
    def decide(self):
        l = [max(set(self.rounds[i][self.id]), key=self.rounds[i][self.id].count) for i in range(m+1)]
        self.order = max(set(l), key=l.count)

    def get_order(self, target_id):
        if self.faction == 0 and target_id % 2 == 0:
            return (self.order + 1) % 2
        else:
            return self.order

    def send_orders(self, round):
        for j in range(n):
            if j != self.id:
                self.rounds[round][self.id].append(generals[j].get_order(self.id))

# iterative approach
def consensous():
    # step 1
    for i in range(1, n):
        generals[i].order = generals[0].get_order(i)

    # step 2
    for round in range(m+1):
        for j in range(1, n):
            generals[j].send_orders(round)

    # step 3
    for i in range(1, n):
        generals[i].decide()

def vote():
    s = sum([gen.order for gen in generals])
    if s < n/2.0:
        results = orders[0]
    else:
        results = orders[1]
    print 'votes: ',
    print ''.join("{} ".format(orders[gen.order]) for gen in generals)
    print "s {}; n {}".format(s, n)
    print("Commander status: {}".format(status[generals[0].faction]))
    print("Overall consensous: {} at dawn!".format(results))


orders = ('ATTACK', 'RETREAT')
status = ('TRAITOR', 'LOYAL')
generals = []
n = 7
num_traitors = 2
m = 2

if __name__=='__main__':
    random.seed(19)
    # do everything 10 times
    for _ in range(10):
        # create generals
        alliance = [0 if i < num_traitors else 1 for i in range(n)]
        random.shuffle(alliance)
        generals = [general(i, alliance[i]) for i in range(n)]

        #print their factions
        print 'factions: ',
        print ''.join("{} ".format(status[gen.faction]) for gen in generals)

        consensous()
        vote()

        print '='*50
        # reset for each iteration
        generals = []

