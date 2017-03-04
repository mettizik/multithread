#!/usr/bin/python3
import CustomThread
import CriticalResource

def incr(resource):
    resource.update(resource.value() + 1)

def decr(resource):
    resource.update(resource.value() - 1)

if __name__ == "__main__":
    res = CriticalResource.SharedResource(0)
    increment_thread = CustomThread.CustomThread(1, "Incrementation thread", res, incr)
    decrement_thread = CustomThread.CustomThread(2, "Decrementation thread", res, decr)
    increment_thread.start()
    decrement_thread.start()
    increment_thread.join()
    import sys
    sys.exit(0)