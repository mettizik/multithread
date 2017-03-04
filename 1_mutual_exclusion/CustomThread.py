#!/usr/bin/python3

import threading

class CustomThread(threading.Thread):
    """
    This class defines a custom thread implementation that does nothing
    """
    _continue = True
    _fails_count = 0
    _ttl = 1024

    def __init__(self, thread_id, name, resource, func):
        threading.Thread.__init__(self)
        self._thread_id = thread_id
        self._name = name
        self._resource = resource
        self._func = func

    def run(self):
        print("[{}] Starting".format(self._name))
        ttl = CustomThread._ttl
        while CustomThread._continue and ttl > 0:
            old_val = self._resource.value()
            print("[{}] old value {}".format(self._thread_id, old_val))
            self._func(self._resource)
            new_val = self._resource.value()
            print("[{}] new value {}".format(self._thread_id, new_val))
            if new_val == old_val:
                CustomThread._continue = False
                CustomThread._fails_count += 1
                print("[{}] value not changed".format(self._thread_id))                
            
            ttl -= 1

        print("[{}] exiting".format(self._name))
