class BitSetException(Exception):
    def __init__(self, message):
        super(BitSetException, self).__init__(message)


class BitSet:

    def __init__(self):
        self._set = 0

    def __str__(self):
        # TODO: rework str representation
        return format(self._set, 'b').zfill(256)

    @staticmethod
    def is_valid_char(char):
        return 0 <= ord(char) < 256

    @property
    def set(self):
        return self._set

    def add(self, char):
        if not BitSet.is_valid_char(char):
            raise BitSetException("Invalid character")
        else:
            pass

    def delete(self, char):
        if not BitSet.is_valid_char(char):
            raise BitSetException("Invalid character")
        else:
            pass


a = BitSet()
print(a)
