#!/usr/bin/python3
import CustomThread
import CriticalResource

def incr(resource):
    resource.update(resource.value() + 1)

def decr(resource):
    resource.update(resource.value() - 1)

if __name__ == "__main__":
    res = CriticalResource.SharedResource(0)
    threads = []
    for i in range(10):        
        threads.append(CustomThread.CustomThread(i + 1, "Incrementation thread #{}".format(i), res, incr))
    for i in range(10, 20):        
        threads.append(CustomThread.CustomThread(i + 1, "Decrementation thread #{}".format(i), res, decr))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("Errors occured: {}".format(CustomThread.CustomThread._fails_count))
