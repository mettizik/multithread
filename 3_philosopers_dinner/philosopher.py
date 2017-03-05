import random
import threading
import time


class RoundTable:
    class PhilosopherIterator(threading.Thread):
        def __init__(self, obj, nxt, prev):
            threading.Thread.__init__(self)
            self.__obj = obj
            self.__next = nxt
            self.__prev = prev

        def run(self):
            while True:
                self.this().think()
                self.this().eat(self)

        def this(self):
            return self.__obj

        def next(self):
            return self.__next

        def prev(self):
            return self.__prev

        def set_next(self, obj):
            self.__next = obj

        def set_prev(self, obj):
            self.__prev = obj

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def append(self, obj):
        if not self.__head:
            self.__head = RoundTable.PhilosopherIterator(obj, obj, obj)
            self.__tail = self.__head
        else:
            new_tail = RoundTable.PhilosopherIterator(
                obj, self.__head, self.__tail)
            self.__tail.set_next(new_tail)
            self.__tail = new_tail
            self.__head.set_prev(self.__tail)

        self.__tail.start()
        self.__size += 1

    def to_list(self):
        if not self.__head:
            return []
        elif self.__size == 1:
            return [self.__head.this()]
        else:
            left = self.__size
            ret = []
            head = self.__head
            while left > 0:
                ret.append(head.this())
                head = head.next()
                left -= 1

            return ret


class Philosopher:
    feeding_time = 3

    def __init__(self, name, power_of_thought):
        self.__thinktime = power_of_thought * 0.1
        self.__name = name
        self.__fork_lock = threading.Lock()
        self.is_eating = False
        self.meals_count = 0

    def _say(self, msg):
        #print("{} : {}".format(self.__name, msg))
        pass

    def eat(self, seat_place):
        self.is_eating = True
        self._say("I'm gonna eat some food")
        neghtboor = seat_place.next().this()
        self._say('{}, can I take your fork?'.format(neghtboor.name()))
        neghtboor.peek_fork()
        self._say('And where is my fork?')
        self.peek_fork()
        time.sleep(self.feeding_time)
        self._say('{}, you can take my fork now'.format(
            seat_place.prev().this().name()))
        self.put_fork()
        self._say('{}, thanks for your fork'.format(neghtboor.name()))
        neghtboor.put_fork()
        self.is_eating = False
        self.meals_count += 1
        self._say("That's enough for now")

    def peek_fork(self):
        self.__fork_lock.acquire()
        self._say('Here is my fork')

    def put_fork(self):
        self._say('Let\s put this fork here')
        self.__fork_lock.release()

    def think(self):
        self._say('Zzzzz...')
        time.sleep(self.__thinktime)

    def name(self):
        return self.__name
