from queue import PriorityQueue

class Node:
    def __init__(self, črka=None, n=None, levi=None, desni=None):
        self.črka = črka
        self.n = n
        self.levi = levi
        self.desni = desni
    def h(self, x):
        if x == '':
            return self.črka
        if x[0] == '0':
            return self.levi.h(x[1:])
        if x[0] == '1':
            return self.desni.h(x[1:])
    def __repr__(self):
        return str(self.črka) + ';' + str(self.n)
    def narisi(self,level=0):
        if self.levi:
            self.levi.narisi(level+1)
        print(level*'         ', self)
        if self.desni:
            self.desni.narisi(level+1)
    def __lt__(self,other):
        return self.n < other.n
    def __rt__(self,other):
        return self.n > other.n
    def __eq__(self,other):
        return self.n == other.n

def frekvence(niz):
    r  = {}
    for znak in niz:
        if znak in r:
            r[znak] += 1
        else:
            r[znak] = 1
    return r

#besedilo
besedilo = 'cabadaba'

#kolikokrat se pojavi kaka črka, vrne v slovarju        
znaki = frekvence(besedilo)
print(znaki)

#iz slovarja znakov nafilamo vrsto s prednostjo
q = PriorityQueue()
for x,y in znaki.items():
    q.put(Node(x,y))

#Po Huffmanu združujemo po dva z najmanjšo pogostostjo
while q.qsize() > 1:
    x = q.get()
    y = q.get()
    nov = Node(x.črka+y.črka, x.n + y.n)
    nov.levi = x
    nov.desni = y
    q.put(nov)

#poberemo zadnjo stvar iz vrste s prednostjo
#to je naše drevo
drevo = q.get()
drevo.narisi()          

