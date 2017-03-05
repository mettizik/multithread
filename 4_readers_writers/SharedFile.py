import time
import threading


class SharedFile:
    def __init__(self, path, delay=0):
        self._file = path
        self._rhandle = None
        self._whandle = None
        self._delay = delay

    def register_reader(self):
        pass

    def unregister_reader(self):
        pass

    def read(self):
        self.register_reader()
        with open(self._file, 'rb') as f:
            data = f.read()
            time.sleep(self._delay)

        self.unregister_reader()
        return data

    def register_writer(self):
        pass

    def unregister_writer(self):
        pass

    def write(self, data):
        self.register_writer()

        with open(self._file, 'wb') as f:
            time.sleep(self._delay * 2)
            f.write(data)

        self.unregister_writer()
