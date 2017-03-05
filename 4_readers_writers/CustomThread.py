#!/usr/bin/python3
import threading
import time


class CustomThread(threading.Thread):
    """
    This class defines a custom thread implementation that does nothing
    """
    tid = 1
    _continue = True
    _indicators = ['-', '\\', '|', '/', '-', '\\', '|', '/']

    def __init__(self, name, resource):
        threading.Thread.__init__(self)
        self._thread_id = CustomThread.tid
        CustomThread.tid += 1
        self._name = name
        self._resource = resource
        self._state = ' '

    def do_action(self, buffer):
        pass

    def use_buffer(self, buffer):
        self._state = '*'
        try:
            self.do_action(buffer)
        except Exception as ex:
            print ("Error in thread #{} [ {} ] - {}".format(
                self._thread_id, self._name, ex))

        self._state = ' '

    def state(self):
        return self._state

    def run(self):
        print("[{}] Starting".format(self._name))
        import random
        import time

        while CustomThread._continue:
            time.sleep(random.randint(1, 5))
            self.use_buffer(self._resource)

        print("[{}] exiting".format(self._name))


class Reader(CustomThread):
    def __init__(self, name, resource):
        CustomThread.__init__(self, name, resource)

    def do_action(self, buffer):
        self._resource.read()


class Writer(CustomThread):
    def __init__(self, name, resource):
        CustomThread.__init__(self, name, resource)

    def do_action(self, buffer):
        time.sleep(1)
        self._resource.write(b"msg")
