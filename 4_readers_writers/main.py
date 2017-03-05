#!/usr/bin/python3
import CustomThread
import time
import SharedFile
import sys

threads_count = 20
if len(sys.argv) > 1:
    threads_count = int(sys.argv[1])

resource = SharedFile.SharedFile('./file.dat', delay=0.5)
threads = []
writers_count = 1

for i in range(writers_count):
    threads.append(CustomThread.Writer("Writer", resource))

for i in range(writers_count, threads_count - writers_count):
    threads.append(CustomThread.Reader("Reader", resource))

for t in threads:
    t.start()

while True:
    time.sleep(0.1)
    resource.display_usage_statistics('\r[ Shared File ] : ')

