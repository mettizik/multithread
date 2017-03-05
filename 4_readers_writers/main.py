#!/usr/bin/python3
import CustomThread
import time

resource = 0
writer = CustomThread.Writer("Writer", resource)
reader = CustomThread.Reader("Reader", resource)

writer.start()
reader.start()

while True:
    time.sleep(0.5)
    print("\r| Reader [{}] | Writer [{}] |".format(
        reader.state(), writer.state()), end='')

