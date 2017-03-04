#!/usr/bin/python3

import threading

class CustomThread(threading.Thread):
    """
    This class defines a custom thread implementation that does nothing
    """

    def __init__(self, thread_id, name):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name

    def run(self):
        print("Starting " + self.name)
        pass
        print("Exiting " + self.name)
