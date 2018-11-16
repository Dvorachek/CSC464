import random

ONE = '1'
ZERO = '0'
UNKNOWN = '?'
FAULTY = 'X'



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
                # self.rounds[round][gen] = dict()
        print self.rounds

        if self.id == 0:
            self.order = random.randint(0, 1)  # commander randomly generates order
            print "Commander's order: {} {}".format(self.order, orders[self.order])  # for my reference
            self.orders_recieved.append(self.order)
            
        else:
            self.order = 1
    
    def majority(self):
        '''l = len(self.orders_recieved)
        s = sum(self.orders_recieved)
        if s > l/2.0:
            self.order = 1
        else:
            self.order = 0'''
        self.order = max(set(self.orders_recieved), key=self.orders_recieved.count)
        #self.orders_recieved = []
        #return self.orders_recieved
    
    def send_order(self, other_general):
        if self.id in other_general.path:
            return
        if self.faction == 0 and other_general.id % 2 == 0:
            #print "I'm traitor-general {} who is sending {} to {}".format(self.id, (self.order + 1) % 2, other_general.id)
            other_general.orders_recieved.append((self.order + 1) % 2)
            other_general.path.append(self.id)
            #other_general.order = (self.order + 1) % 2
        else:
            other_general.orders_recieved.append(self.order)
            other_general.path.append(self.id)
            #other_general.order = self.order

        print other_general.path
        print other_general.orders_recieved
        '''for i, p in enumerate(self.path[1:]):
            print type(p)
            test = set([x for x in p if p.count(x) > 1])
            if test:
                del other_general.orders_recieved[i]
                del other_general.path[i]'''
    
    def get_order(self, target_id):
        if self.faction == 0 and target_id % 2 == 0:
            value = (self.order + 1) % 2
        else:
            value = self.order


    def send_orders(self, round):
        for i in range(len(self.rounds[round][self.id])):
            for j in range(n):
                if j != self.id:
                    if generals[j].faction == 0 and self.id % 2 == 0:
                        value = (generals[j].order + 1) % 2
                    else:
                        value = generals[j].order

                    self.rounds[round][self.id].append(value)
                    #self.rounds[round][self.id][j] = value


def communicate(command, iteration):
    if iteration == m:
        for i in range(1, n):
            if i == command:
                continue
            generals[command].send_order(generals[i])
        
        [general.majority() for general in generals[1:]]

    else:
        for i in range(1, n):
            if i == command:
                continue
            generals[command].send_order(generals[i])
        for i in range(1, n):
            if i == command:
                continue
            communicate(i, iteration + 1)
        [general.majority() for general in generals[1:]]

def alg(command, iteration):
    if iteration == m:
        for i in range(1, n):
            if i == command:
                continue
            generals[command].send_order(generals[i])

    else:
        for i in range(1, n):
            if i == command:
                continue
            generals[command].send_order(generals[i])
            alg(i, iteration + 1)

        #print "{}; {}".format(command, generals[command].orders_recieved)
        if command != 0:
            generals[command].majority()
        print "\n{}; {}; {}".format(command, generals[command].order, generals[command].orders_recieved)

def a2():
    #step 1
    commander_message()
    [generals[0].send_order(i) for i in range(1, n)]

    for i in range(m+1):
        for j in range(1, n):
            generals[j].send_orders(i)
            print generals[j].rounds


def commander_message():
    [generals[0].send_order(i) for i in range(1, n)]
        

def vote():
    s = sum([gen.order for gen in generals])
    if s < n/2.0:
        results = orders[0]
    else:
        results = orders[1]
    print [gen.order for gen in generals]
    print "s {}; n {}".format(s, n)
    
    '''results = [0, 0]
    for gen in generals:
        results[gen.order] += 1

    print "Results of vote are {}".format(results)
    print ''.join("{} ".format(gen.order) for gen in generals)

    if results[0] > results[1]:
        results = orders[0]
    else:
        results = orders[1]
    '''
    print("Commander status: {}".format(status[generals[0].faction]))
    print("Overall consensous: {} at dawn!".format(results))


orders = ('ATTACK', 'RETREAT')
status = ('TRAITOR', 'LOYAL')
generals = []
n = 7
num_traitors = 2
m = 2


if __name__=='__main__':
    random.seed(13)

    for _ in range(10):  # do everything 10 times
        alliance = [1 for _ in range(n-num_traitors)]
        [alliance.append(0) for _ in range(num_traitors)]
        random.shuffle(alliance)
        generals = [general(i, alliance[i]) for i in range(n)]
        '''for i in range(n):
            if num_traitors:
                g = general(i, abs(random.randint(-1, 1)))
                generals.append(g)
                if g.faction == 0:
                    num_traitors -= 1
            else:
                generals.append(general(i, 1))'''

        print ''.join("{} ".format(gen.faction) for gen in generals)
        a2()
        #alg(0, 0)
        #vote()
        print '='*50
        generals = []
