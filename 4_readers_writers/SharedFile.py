import time
import threading


class SharedFile:
    def __init__(self, path, delay=0):
        self._file = path
        self._delay = delay
        self._read_lock = threading.Lock()
        self._read_switch = _CompositeLock()
        self._readers = 0
        self._writers = 0
        self._statistics_lock = threading.Lock()

    def display_usage_statistics(self, presymbol):
        with self._statistics_lock:
            print('{} || Readers: {} || || Writers: {} ||'.format(
                presymbol, self._readers, self._writers), flush=True, end='')
            if self._readers > 0 and self._writers > 0:
                print("Error! Readers and writers are using resource at the same time!")
            if self._writers > 1:
                print("Error! To many writers are using resource at the same time!")

    def register_reader(self):
        self._read_switch.acquire(self._read_lock)
        with self._statistics_lock:
            self._readers += 1

    def unregister_reader(self):
        with self._statistics_lock:
            self._readers -= 1
        self._read_switch.release(self._read_lock)

    def read(self):
        self.register_reader()
        with open(self._file, 'rb') as f:
            data = f.read()
            time.sleep(self._delay)

        self.unregister_reader()
        return data

    def register_writer(self):
        self._read_switch.lock(self._read_lock)
        with self._statistics_lock:
            self._writers += 1

    def unregister_writer(self):
        with self._statistics_lock:
            self._writers -= 1
        self._read_switch.unlock(self._read_lock)

    def write(self, data):
        self.register_writer()

        with open(self._file, 'wb') as f:
            time.sleep(self._delay * 4)
            f.write(data)

        self.unregister_writer()


class _CompositeLock:
    def __init__(self):
        self.__counter = 0
        self.__mutex = threading.Lock()
        self.__general_lock = threading.Lock()

    def lock(self, lock):
        self.__general_lock.acquire()
        lock.acquire()

    def unlock(self, lock):
        lock.release()
        self.__general_lock.release()

    def acquire(self, lock):
        with self.__general_lock:
            self.__mutex.acquire()
            self.__counter += 1
            if self.__counter == 1:
                lock.acquire()
            self.__mutex.release()

    def release(self, lock):
        self.__mutex.acquire()
        self.__counter -= 1
        if self.__counter == 0:
            lock.release()
        self.__mutex.release()