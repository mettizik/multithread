#!/usr/bin/python3
import CustomThread
import time
import SharedFile

resource = SharedFile.SharedFile('./file.dat', delay=0.5)
w0 = CustomThread.Writer("Writer", resource)
w1 = CustomThread.Writer("Writer", resource)
r0 = CustomThread.Reader("Reader", resource)
r1 = CustomThread.Reader("Reader", resource)
r2 = CustomThread.Reader("Reader", resource)

w0.start()
w1.start()
r0.start()
r1.start()
r2.start()

while True:
    print("\r| R0 [{}] | R1 [{}] | R2 [{}] | W0 [{}] | W1 [{}] |".format(
        r0.state(), r1.state(), r2.state(), w0.state(), w1.state()), end='', flush=True)

