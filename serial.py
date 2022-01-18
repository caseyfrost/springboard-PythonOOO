"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Constructs the generator object with two attributes

        Parameters:
            1. _start - starting number, must be an int or float.
            2. _current - stores the current number after it was generated.
                         current = start - 1 because the generator method
                         increments current by one"""
        self._start = start
        self._current = start - 1

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, start):
        if isinstance(self._start, int) or isinstance(self._start, float):
            self._start = start
        else:
            raise TypeError('Input must me a number')

    @property
    def current(self):
        return self._current

    def generate(self):
        """Increments current by one and returns the new value of current"""
        self._current += 1
        return self._current

    def reset(self):
        """Resets the value of current to start - 1"""
        self._current = self._start - 1

    def __repr__(self):
        rep = f'<Start={self._start} Next={self._current + 1}>'
        return rep


if __name__ == '__main__':
    test = SerialGenerator(100)
    print(repr(test))
    test.generate()
    print(repr(test))
    help(SerialGenerator)
