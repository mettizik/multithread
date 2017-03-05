import time


class SharedFile:
    def __init__(self, path, delay=0):
        self._file = path
        self._rhandle = None
        self._whandle = None
        self._delay = delay
        self._readers = 0
        self._writers = 0

    def read(self):
        self._readers += 1
        if self._writers > 0:
            print("Reading while writing!")
        if not self._rhandle:
            self._rhandle = open(self._file, mode='rb')

        data = self._rhandle.read()
        time.sleep(self._delay)
        self._readers -= 1
        if self._readers == 0:
            self._rhandle.close()
            self._rhandle = None

        return data

    def write(self, data):
        self._writers += 1
        if self._whandle or self._writers > 1:
            print("More than one writer!")

        if self._readers > 0:
            print("Writing while reading!")

        with open(self._file, 'wb') as self._whandle:
            time.sleep(self._delay * 2)
            self._whandle.write(data)

        self._writers -= 1
        self._whandle = None
