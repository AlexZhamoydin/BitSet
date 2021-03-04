class BitSetException(Exception):
    def __init__(self, message):
        super(BitSetException, self).__init__(message)


class BitSet:
    def __init__(self):
        self._set = 0

    def __str__(self):
        return format(self._set, 'b').zfill(256)

    @property
    def set(self):
        return self._set

    def add(self, char):
        pass

    def delete(self, char):
        pass


a = BitSet()
print(a)


