#!/usr/bin/python3

import threading

class CustomThread(threading.Thread):
    """
    This class defines a custom thread implementation that does nothing
    """
    cont = True
    def __init__(self, thread_id, name, resource, func):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self._resource = resource
        self._func = func

    def run(self):
        while CustomThread.cont:
            print("[{}] Starting".format(self.name))
            while True:
                old_val = 0 + self._resource.value()
                print("[{}] old value {}".format(self.thread_id, old_val))
                self._func(self._resource)
                new_val = 0 + self._resource.value()
                print("[{}] new value {}".format(self.thread_id, new_val))
                if new_val == old_val:
                    CustomThread.cont = False
                    raise RuntimeError("Value not changed")
            
            print("[{}] exiting".format(self.name))
