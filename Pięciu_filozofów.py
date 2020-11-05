#Zadanie Pięciu filozofów wersja bez deadlocka
import time
import sys
import threading

class Fork(object):
    def __init__(self, num):
        self.number = num
        self.user = -1
        self.lock = threading.Condition(threading.Lock())
        self.taken = False

    def drop_fork(self, user):
        with self.lock:
            while self.taken == False:
                self.lock.wait()
            self.user = -1
            self.taken = False
            sys.stdout.write("Filozof[ %s ] odłożył widelec[ %s ]\n" % (user, self.number))
            self.lock.notifyAll()

    def take_fork(self, user):
        with self.lock:
            while self.taken == True:
                self.lock.wait()
            self.user = user
            self.taken = True
            sys.stdout.write("Filozof[ %s ] podniósł widelec[ %s ]\n" % (user, self.number))
            self.lock.notifyAll()

class Philosopher(threading.Thread):
    def __init__(self, number, left, right, waiter):
        threading.Thread.__init__(self)
        self.number = number
        self.left = left
        self.right = right
        self.waiter = waiter

    def run(self):
        for i in range(20):
            time.sleep(1)                        #myśli
            self.left.take_fork(self.number)     #bierze lewy widelec
            time.sleep(1)
            self.right.take_fork(self.number)    #bierze prawy widelec
            time.sleep(1)                        #je posiłek
            self.right.drop_fork(self.number)    #odkłada prawy widelec
            self.left.drop_fork(self.number)     #odkłada lewy widelec
        sys.stdout.write("-----Filozof[ %s ] skończył posiłek oraz dyskusję-----\n" % self.number)

forks = []
philosophers = []

for i in range(0, 5):
    forks.append(Fork(i))

for i in range(0, 5):
    philosophers.append(Philosopher(i, forks[i], forks[(i+1)%5], 0))

for i in range(5):
    philosophers[i].start()