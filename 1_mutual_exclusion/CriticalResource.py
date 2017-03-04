class SharedResource:
    """
    This class represents a resource that can be share in mulitthreaded environment
    It provides a synchronized access to the shared object
    """

    def __init__(self, value):
        self._value = value

    def update(self, new_value):
        self._value = new_value

    def value(self):
        return self._value
